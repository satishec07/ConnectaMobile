import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import inspect
import logging


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logFile.log')
        logger.addHandler(fileHandler)  # file handler object     ****************************************
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.setLevel(logging.DEBUG)

        return logger

    def selectionOptionByText(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_value(text)

    def implicitlyWaitTime(self, time=6):
        self.driver.implicitly_wait(time)

    # def pageScroll(self, driver):
    #     driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")

    def waitById(self, text, time=10):
        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.presence_of_element_located((By.ID, text)))

    def waitByXPATH(self, text, time=10):
        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, text)))

    def waitElement_Clickable(self, text, time=10):

        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.element_to_be_clickable((By.ID, text)))

    def pageScroll(self, driver, element):
        driver.execute_script("arguments[0].scrollIntoView(true)", element)

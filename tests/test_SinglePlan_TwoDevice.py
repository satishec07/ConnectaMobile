import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.DevicePlanPage import DevicePlan
from utilities.BaseClass import BaseClass


class TestMoreDevice_Plan(BaseClass):
    def test_SinglePlan_TwoDevice(self):
        self.driver.maximize_window()
        self.implicitlyWaitTime(5)
        Dplan = DevicePlan(self.driver)
        # Dplan.getPlanPage().click()
        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.selectionOptionByText(Dplan.getPlanLines(), "1")
        Dplan.getAddPlan().click()
        # Dplan.getAllDevice().click()
        Dplan.getDevice1().click()
        Dplan.getAdd_toCard().click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class='swal-title']")))
        Add_toCard_Message = Dplan.getAdd_toCard_Message().text
        print("Add_toCard_Message", Add_toCard_Message)
        assert "successfully" in Add_toCard_Message
        Dplan.getAdd_More_Device().click()
        Add_toCard_Message = Dplan.getAdd_toCard_Message().text
        print("Add_toCard_Message", Add_toCard_Message)
        assert "You've reached the device limit. The number of devices cannot exceed the number of lines." in Add_toCard_Message











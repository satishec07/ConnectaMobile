import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.DevicePlanPage import DevicePlan
from utilities.BaseClass import BaseClass


class TestDevicePlan(BaseClass):
    def test_DevicePlan(self):
        self.driver.maximize_window()
        self.implicitlyWaitTime(5)
        Dplan = DevicePlan(self.driver)
        # Dplan.getPlanPage().click()
        self.pageScroll(self.driver, Dplan.getPlanLines())
        # self.driver.execute_script("window.scrollBy(0, 1000);")
        self.selectionOptionByText(Dplan.getPlanLines(), "1")
        Dplan.getAddPlan().click()
        # Dplan.getAllDevice().click()
        self.pageScroll(self.driver, Dplan.getDevice1())
        Dplan.getDevice1().click()
        Dplan.getAdd_toCard().click()
        Dplan.getGo_toCard().click()
        self.pageScroll(self.driver, Dplan.getBilling_Zip())
        Dplan.getBilling_Zip().send_keys("30344")
        Dplan.getUpdate_Button().click()
        self.pageScroll(self.driver, Dplan.getProceed_toCheckout())
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Proceed to Checkout']")))
        Dplan.getProceed_toCheckout().click()
        Dplan.getEmail().send_keys("testorder@vcaremail.com")
        Dplan.getPhone().send_keys("1234567890")
        # self.driver.execute_script("window.scrollBy(0, 500);")
        Dplan.get_Continue_Page().click()
        self.pageScroll(self.driver, Dplan.get_eBillingAddress1())
        Dplan.get_eBillingAddress1().send_keys("2982 DUKE OF WINDSOR")
        # Dplan.get_eBillingAddress2().click()
        # try:
        #     wait = WebDriverWait(self.driver, 10)
        #     wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Proceed']")))
        # except Exception as e:
        #     print(e)
        #
        # try:
        #     Dplan.get_Address_suggetion().click()
        # except Exception as e:
        #     print(e)
        self.pageScroll(self.driver, Dplan.getShippingMethod())
        # self.driver.execute_script("window.scrollBy(0, 900);")
        Dplan.getShippingMethod().click()
        self.selectionOptionByText(Dplan.getHear_About(), "14")
        Dplan.getAfter_shipping_Continue().click()
        self.pageScroll(self.driver, Dplan.getName_onCard())
        # self.driver.execute_script("window.scrollBy(0, 1500);")
        Dplan.getName_onCard().send_keys("TestCard")
        Dplan.getCard_Number().send_keys("4111111111111111")
        self.selectionOptionByText(Dplan.getExp_Month(), "03")
        self.selectionOptionByText(Dplan.getExp_Year(), "2026")
        Dplan.getCard_CVV().send_keys("231")
        Dplan.getAfterCard_Continue().click()

        portinpage = self.driver.find_element(By.XPATH, "//button[contains(@onclick, 'validate_portin_linewise')]")
        self.pageScroll(self.driver, portinpage)

        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.ID, "fifth")))

        Dplan.getAfter_TransfPhone_Continue().click()
        self.pageScroll(self.driver, Dplan.getFirst_Name())
        self.waitElement_Clickable("fname", 10)
        Dplan.getFirst_Name().send_keys("Test")
        Dplan.getLast_Name().send_keys("Order")
        Dplan.getPassword().send_keys("Test@12345")
        self.selectionOptionByText(Dplan.getSecurity_Ques(), "What was your favorite subject in school?")
        Dplan.getSecurity_Ans().send_keys("TestOrder")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.ID, "agreed_doc")))

        self.pageScroll(self.driver, Dplan.getAgree_TC())
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.ID, "agreed_doc")))

        Dplan.getAgree_TC().click()
        # assert Dplan.getAgree_TC().is_selected()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.ID, "validate_amt")))
        self.pageScroll(self.driver, Dplan.getPlace_Order())
        Dplan.getPlace_Order().click()
        wait = WebDriverWait(self.driver, 14)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "h2.mainTittle.cart.cloudSafe")))
        message = Dplan.getOrder_Message().text
        print("Message ", message)
        assert "Thank you for your order!" == message

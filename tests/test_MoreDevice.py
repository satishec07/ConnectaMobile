import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.DevicePlanPage import DevicePlan
from utilities.BaseClass import BaseClass


class TestMoreDevice_Plan(BaseClass):
    def test_MoreDevices_Plan(self):
        self.driver.maximize_window()
        self.implicitlyWaitTime(5)
        Dplan = DevicePlan(self.driver)
        # Dplan.getPlanPage().click()
        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.selectionOptionByText(Dplan.getPlanLines(), "2")
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
        Dplan.getDevice2().click()
        Dplan.getAdd_toCard().click()
        Dplan.getGo_toCard().click()
        Dplan.getBilling_Zip().send_keys("30344")
        Dplan.getUpdate_Button().click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Proceed to Checkout']")))
        Dplan.getProceed_toCheckout().click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@id='email']")))
        Dplan.getEmail().send_keys("TestOrder@vcaremail.com")
        Dplan.getPhone().send_keys("1234567890")
        self.driver.execute_script("window.scrollBy(0, 500);")
        Dplan.get_Continue_Page().click()
        Dplan.get_eBillingAddress1().send_keys("2982 DUKE OF WINDSOR")
        Dplan.get_eBillingAddress2().click()
        try:
            wait = WebDriverWait(self.driver, 5)
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Proceed']")))
        except Exception as e:
            print(e)

        try:
            Dplan.get_Address_suggetion().click()
        except Exception as e:
            print(e)

        self.driver.execute_script("window.scrollBy(0, 900);")
        Dplan.getShippingMethod().click()
        self.selectionOptionByText(Dplan.getHear_About(), "14")
        Dplan.getAfter_shipping_Continue().click()
        self.driver.execute_script("window.scrollBy(0, 1500);")
        Dplan.getName_onCard().send_keys("TestCard")
        Dplan.getCard_Number().send_keys("4111111111111111")
        self.selectionOptionByText(Dplan.getExp_Month(), "03")
        self.selectionOptionByText(Dplan.getExp_Year(), "2026")
        Dplan.getCard_CVV().send_keys("231")
        # self.driver.execute_script("window.scrollBy(0, 2200);")
        Dplan.getAfterCard_Continue().click()
        self.driver.execute_script("window.scrollBy(0, 2200);")
        time.sleep(3)

        ########################################################
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.ID, "fifth")))
        Dplan.getAfter_TransfPhone_Continue().click()
        self.driver.execute_script("window.scrollBy(0, 1200);")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.ID, "fname")))
        Dplan.getFirst_Name().send_keys("Test")
        Dplan.getLast_Name().send_keys("Order")
        Dplan.getPassword().send_keys("Test@12345")
        self.driver.execute_script("window.scrollBy(0, 500);")
        self.selectionOptionByText(Dplan.getSecurity_Ques(), "What was your favorite subject in school?")
        Dplan.getSecurity_Ans().send_keys("TestOrder")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.ID, "agreed_doc")))
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable((By.ID, "agreed_doc")))
        Dplan.getAgree_TC().click()
        assert Dplan.getAgree_TC().is_selected()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.ID, "validate_amt")))
        Dplan.getPlace_Order().click()
        wait = WebDriverWait(self.driver, 14)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "h2.mainTittle.cart.cloudSafe")))
        message = Dplan.getOrder_Message().text
        print("Message ", message)
        assert "Thank you for your order!" == message

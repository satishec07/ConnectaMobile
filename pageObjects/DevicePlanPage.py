from selenium.webdriver.common.by import By


class DevicePlan:
    def __init__(self, driver):
        self.driver = driver

    planPage = (By.XPATH, "(//a[text()='Plans'])[1]")
    planLines = (By.XPATH, "//div[@class='row']//div[1]//div[1]//div[1]//ul[2]//li[1]//div[1]//select[1]")
    addPlan = (By.ID, "plan_list_1171")
    allDevice = (By.LINK_TEXT, "All")
    skip_Device = (By.CSS_SELECTOR, ".loadernew")
    device1 = (By.XPATH, "(//img[@title='Product Image'])[7]")
    add_toCard = (By.XPATH, "//button[text()='Add to cart']")
    go_toCard = (By.XPATH, "//button[text()='Go to Cart']")
    go_ToPlanPage = (By.XPATH, "//button[text()='Go to Plan Page']")
    add_toCard_Message = (By.XPATH, "//div[@class='swal-title']")
    add_More_Device = (By.XPATH, "//button[text()='Add more Device']")
    device2 = (By.XPATH, "(//img[@title='Product Image'])[7]")

    billing_Zip = (By.ID, "enroll_zip")
    update_Button = (By.XPATH, "//button[text()='Update']")
    promoCode = (By.ID, "coupon_fields")
    apply_promoCode = (By.ID, "apply_coupon")
    proceed_toCheckout = (By.XPATH, "//button[text()='Proceed to Checkout']")
    email = (By.ID, "email")
    phone = (By.ID, "phone_number")
    continue_Page = (By.XPATH, "(//button[text()='Continue'])[1]")
    eBillingAddress1 = (By.ID, "e_billing_address1")
    # address_suggetion = (By.XPATH, "//button[text()='Proceed']")
    eBillingAddress2 = (By.ID, "e_billing_address2")
    shippingMethod = (By.XPATH, "//input[@value='2']")
    hear_About = (By.ID, "hear_us")
    address_suggetion = (By.XPATH, "//button[text()='Proceed']")
    after_shipping_Continue = (By.XPATH, "(//button[text()='Continue'])[2]")
    name_onCard = (By.ID, "card_holder_name")
    card_Number = (By.ID, "card_number")
    exp_Month = (By.ID, "exp_mon")
    exp_Year = (By.ID, "exp_year")
    card_CVV = (By.ID, "cvv")
    afterCard_Continue = (By.ID, "fourth")
    after_TransfPhone_Continue = (By.ID, "fifth")
    first_Name = (By.ID, "fname")
    last_Name = (By.ID, "lname")
    password = (By.ID, "pin-password")
    security_Ques = (By.ID, "security-question")
    security_Ans = (By.ID, "security-answer")
    agree_TC = (By.ID, "agreed_doc")
    place_Order = (By.ID, "validate_amt")
    order_Message = (By.CSS_SELECTOR, "h2.mainTittle.cart.cloudSafe")

    def getPlanPage(self):
        return self.driver.find_element(*DevicePlan.planPage)

    def getPlanLines(self):
        return self.driver.find_element(*DevicePlan.planLines)

    def getAddPlan(self):
        return self.driver.find_element(*DevicePlan.addPlan)

    def getAllDevice(self):
        return self.driver.find_element(*DevicePlan.allDevice)

    def get_skip_Device(self):
        return self.driver.find_element(*DevicePlan.skip_Device)

    def getDevice1(self):
        return self.driver.find_element(*DevicePlan.device1)

    def getAdd_toCard(self):
        return self.driver.find_element(*DevicePlan.add_toCard)

    def getGo_toCard(self):
        return self.driver.find_element(*DevicePlan.go_toCard)

    def getGo_ToPlanPage(self):
        return self.driver.find_element(*DevicePlan.go_ToPlanPage)

    def getAdd_toCard_Message(self):
        return self.driver.find_element(*DevicePlan.add_toCard_Message)

    def getAdd_More_Device(self):
        return self.driver.find_element(*DevicePlan.add_More_Device)

    def getDevice2(self):
        return self.driver.find_element(*DevicePlan.device2)

    def getBilling_Zip(self):
        return self.driver.find_element(*DevicePlan.billing_Zip)

    def getUpdate_Button(self):
        return self.driver.find_element(*DevicePlan.update_Button)

    def getPromoCode(self):
        return self.driver.find_element(*DevicePlan.promoCode)

    def getApply_promoCode(self):
        return self.driver.find_element(*DevicePlan.apply_promoCode)

    def getProceed_toCheckout(self):
        return self.driver.find_element(*DevicePlan.proceed_toCheckout)

    def getEmail(self):
        return self.driver.find_element(*DevicePlan.email)

    def getPhone(self):
        return self.driver.find_element(*DevicePlan.phone)

    def get_Continue_Page(self):
        return self.driver.find_element(*DevicePlan.continue_Page)

    def get_eBillingAddress1(self):
        return self.driver.find_element(*DevicePlan.eBillingAddress1)

    # def get_Address_suggetion(self):
    #     return self.driver.find_element(*DevicePlan.address_suggetion)

    def get_eBillingAddress2(self):
        return self.driver.find_element(*DevicePlan.eBillingAddress2)

    def getShippingMethod(self):
        return self.driver.find_element(*DevicePlan.shippingMethod)

    def getHear_About(self):
        return self.driver.find_element(*DevicePlan.hear_About)

    def get_Address_suggetion(self):
        return self.driver.find_element(*DevicePlan.address_suggetion)

    def getAfter_shipping_Continue(self):
        return self.driver.find_element(*DevicePlan.after_shipping_Continue)
###############################################################################
    def getName_onCard(self):
        return self.driver.find_element(*DevicePlan.name_onCard)

    def getCard_Number(self):
        return self.driver.find_element(*DevicePlan.card_Number)

    def getExp_Month(self):
        return self.driver.find_element(*DevicePlan.exp_Month)

    def getExp_Year(self):
        return self.driver.find_element(*DevicePlan.exp_Year)

    def getCard_CVV(self):
        return self.driver.find_element(*DevicePlan.card_CVV)

    def getAfterCard_Continue(self):
        return self.driver.find_element(*DevicePlan.afterCard_Continue)

    def getAfter_TransfPhone_Continue(self):
        return self.driver.find_element(*DevicePlan.after_TransfPhone_Continue)

    def getFirst_Name(self):
        return self.driver.find_element(*DevicePlan.first_Name)

    def getLast_Name(self):
        return self.driver.find_element(*DevicePlan.last_Name)

    def getPassword(self):
        return self.driver.find_element(*DevicePlan.password)

    def getSecurity_Ques(self):
        return self.driver.find_element(*DevicePlan.security_Ques)

    def getSecurity_Ans(self):
        return self.driver.find_element(*DevicePlan.security_Ans)

    def getAgree_TC(self):
        return self.driver.find_element(*DevicePlan.agree_TC)

    def getPlace_Order(self):
        return self.driver.find_element(*DevicePlan.place_Order)

    def getOrder_Message(self):
        return self.driver.find_element(*DevicePlan.order_Message)







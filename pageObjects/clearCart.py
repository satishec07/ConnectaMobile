"""
1. single plan,  each time clear cart
2. two line plan only
3  single line and single device
4. single line and two device
5. two line  and single device
6. two line  and two device
7. two line and three device
"""
from selenium.webdriver.common.by import By


class clearCard:
    def __init__(self, driver):
        self.driver = driver

    cart = (By.XPATH, "//img[@title='Cart']")
    clear_Card = (By.CSS_SELECTOR, ".clearCart")
    accept_OK = (By.XPATH, "//button[text()='OK']")






    def gerCard(self):
        return self.driver.find_element(*clearCard.cart)

    def getClearCard(self):
        return self.driver.find_element(*clearCard.clear_Card)
    
    def getAcceptAsOK(self):
        return self.driver.find_element(*clearCard.accept_OK)

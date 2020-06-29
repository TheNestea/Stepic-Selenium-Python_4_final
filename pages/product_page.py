import math
import time
from .base_page import BasePage
from .locators import BasePageLocators
#from .locators import MainPageLocators
from .locators import ProductPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_product_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

        self.solve_quiz_and_get_code()

        product_name_was_added = self.browser.find_element(*ProductPageLocators.ALERT_PRODUCT_WAS_ADDED).text
        assert product_name == product_name_was_added, "Incorrect product names in basket, AR = " + product_name_was_added + ", ER = " + product_name

        #time.sleep(15000)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_PRODUCT_WAS_ADDED), "Success message is presented, but should not be"

    def success_message_should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_PRODUCT_WAS_ADDED), "Button is not disappeared, but should be"

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "Wrong login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTR_EMAIL), "Reg email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTR_PASSWORD_1), "Reg password_1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTR_PASSWORD_2), "Reg repeat password_2 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTR_BUTTON), "Reg button is not presented"

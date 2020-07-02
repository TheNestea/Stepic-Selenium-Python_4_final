from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        assert "http://selenium1py.pythonanywhere.com/" in self.browser.current_url, "Wrong URL domain in \"" + self.browser.current_url + "\""
        assert "/accounts/login/" in self.browser.current_url, "Wrong URL path in \"" + self.browser.current_url + "\""


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTR_EMAIL), "Reg email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTR_PASSWORD_1), "Reg password_1 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTR_PASSWORD_2), "Reg repeat password_2 is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTR_BUTTON), "Reg button is not presented"


    def register_new_user(self, email, password):
        register_email = self.browser.find_element(*LoginPageLocators.REGISTR_EMAIL)
        register_email.send_keys(email)
        register_pass1 = self.browser.find_element(*LoginPageLocators.REGISTR_PASSWORD_1)
        register_pass1.send_keys(password)
        register_pass2 = self.browser.find_element(*LoginPageLocators.REGISTR_PASSWORD_2)
        register_pass2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTR_BUTTON).click()

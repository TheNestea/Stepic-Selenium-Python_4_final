from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name=\"login_submit\"]")

    REGISTR_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTR_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTR_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTR_BUTTON = (By.CSS_SELECTOR, "[name=\"registration_submit\"]")

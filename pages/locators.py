from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_WITH_PRODUCT = (By.CSS_SELECTOR, "#content_inner .basket-title")
    PAGE_HEADER = (By.CSS_SELECTOR, ".page-header.action")


class MainPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn:nth-child(1)")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name=\"login_submit\"]")

    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name=\"registration_submit\"]")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    ALERT_PRODUCT_WAS_ADDED = (By.CSS_SELECTOR, "#messages > .alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "some test purpose CSS_SELECTOR")

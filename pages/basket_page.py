from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        assert "/basket/" in self.browser.current_url, "Wrong URL path in \"" + self.browser.current_url + "\""
        assert self.is_element_present(*BasketPageLocators.PAGE_HEADER), "PAGE_HEADER is not presented"


    def should_be_empty_basket_page(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_WITH_PRODUCT)

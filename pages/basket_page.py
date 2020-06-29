from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        assert self.is_element_present(*BasketPageLocators.PAGE_HEADER), "PAGE_HEADER is not presented"
        assert self.browser.find_element(*BasketPageLocators.PAGE_HEADER).text == "Корзина", "Название экрана не Корзина"

    def should_be_empty_basket_page(self):
        empty_basket = self.browser.find_element(*BasketPageLocators.EMPTY_BUSKET)
        assert empty_basket.text == "Ваша корзина пуста Продолжить покупки", "Отличается текст пустой корзины " + empty_basket.text

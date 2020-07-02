# pytest -v --tb=line --language=en test_main_page.py

import pytest
import time
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                             # открываем страницу
        page.go_to_login_page()                 # выполняем метод страницы - переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

        email = str(time.time()) + "@fakemail.org"
        password = "087a3efacf10"
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()


    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                             # открываем страницу
        page.should_not_be_success_message()    # проверяем что нет собщения об успехе


    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                             # открываем страницу
        page.add_product_to_basket()            # выполняем метод страницы - добавляем товар в корзину и проверяем успешность добавления


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()                             # открываем страницу
    page.add_product_to_basket()            # выполняем метод страницы - добавляем товар в корзину и проверяем успешность добавления


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # открываем страницу
    page.add_product_to_basket()            # выполняем метод страницы - добавляем товар в корзину и проверяем успешность добавления
    page.should_not_be_success_message()    # проверяем что нет собщения об успехе


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # открываем страницу
    page.should_not_be_success_message()    # проверяем что нет собщения об успехе


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # открываем страницу
    page.add_product_to_basket()            # выполняем метод страницы - добавляем товар в корзину и проверяем успешность добавления
    page.success_message_should_disappeared()    # проверяем что нет собщения об успехе


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_be_empty_basket_page()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                             # открываем страницу
    page.go_to_login_page()                 # выполняем метод страницы - переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# pytest -v --tb=line --language=en test_main_page.py
# pytest -v --tb=line --language=en -m login_guest test_main_page.py

from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)                          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                                             # открываем страницу
        page.go_to_login_page()                                 # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)    # передаем объект драйвера для работы с
        # браузером, а в качестве url передаем текущий адрес
        login_page.should_be_login_page()                       # проверка на корректный url адрес
        # should_be_login_url из login_page.py

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()

# Гость открывает главную страницу
# Переходит в корзину по кнопке в шапке сайта
# Ожидаем, что в корзине нет товаров
# Ожидаем, что есть текст о том что корзина пуста
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = MainPage(browser, link)
    page.open()  # Гость открывает главную страницу
    page.go_to_basket_page()  # Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)  # Объект страницы корзины
    basket_page.should_not_be_product_in_basket()  # Ожидаем, что в корзине нет товаров
    basket_page.should_be_message_about_empty_basket()  # Ожидаем, что есть текст о том что корзина пуста


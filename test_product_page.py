# pytest -v -s --tb=line --language=en test_product_page.py

from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import time
import pytest

@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    page = ProductPage(browser, link)       # инициализировать Page Object, передать в конструктор экземпляр драйвера и url адрес
    page.open()                             # открыть страницу
    page.should_be_add_to_basket()          # проверить есть ли в карточке товара - Кнопка, цена, наименование товара
    page.product_add_to_basket()            # в карточке товара - цена, наименование товара
    page.press_add_to_basket_button()       # нажать кнопку "Добавить в корзину"
    page.solve_quiz_and_get_code()          # в алерте считать х, найти результат функции и получить ответ - реализация степик
    page.should_product_in_basket()         # проверить есть ли в корзине - общая стоимость, наименование товара
    page.product_in_basket()                # в корзине - общая стоимость, наименование товара
    page.product_comparison()               # сравнить наименование и стоимость товара в карточке и корзине

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)       # инициализировать Page Object, передать в конструктор экземпляр драйвера и url адрес
    page.open()                             # открыть страницу
    page.product_add_to_basket()            # в карточке товара - цена, наименование товара
    page.press_add_to_basket_button()       # нажать кнопку "Добавить в корзину"
    page.should_be_message_about_success()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)       # инициализировать Page Object, передать в конструктор экземпляр драйвера и url адрес
    page.open()                             # открыть страницу
    page.product_add_to_basket()            # в карточке товара - цена, наименование товара
    page.should_be_message_about_success()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)       # инициализировать Page Object, передать в конструктор экземпляр драйвера и url адрес
    page.open()                             # открыть страницу
    page.product_add_to_basket()            # в карточке товара - цена, наименование товара
    page.press_add_to_basket_button()       # нажать кнопку "Добавить в корзину"
    page.should_be_message_of_is_disappeared()

# тесты вида "гость может перейти на страницу логина со страницы Х"
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# тесты вида "гость может перейти на страницу логина со страницы Х"
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

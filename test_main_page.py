# pytest -v --tb=line --language=en test_main_page.py

from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
# из файла login_page.py импортируйте класс LoginPage
from .pages.login_page import LoginPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                                             # открываем страницу
    page.go_to_login_page()                                 # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)    # передаем объект драйвера для работы с браузером, а в качестве url передаем текущий адрес
    login_page.should_be_login_page()                       # проверка на корректный url адрес should_be_login_url из login_page.py
    # print("**************** 3")
    # time.sleep(3)




def test_guest_should_see_login_link(browser):
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

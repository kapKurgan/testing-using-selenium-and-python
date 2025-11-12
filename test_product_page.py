# pytest -v -s --tb=line --language=en test_product_page.py

from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)       # инициализировать Page Object, передать в конструктор экземпляр драйвера и url адрес
    page.open()                             # открыть страницу
    page.should_be_button_add_to_basket()   # проверить есть ли кнопка "Добавить в корзину"
    page.press_button_add_to_basket()       # нажать кнопку "Добавить в корзину"
#    page.view_alert_math()                 # в алерте считать х, найти результат функции и получить ответ - реализация моя
    page.solve_quiz_and_get_code()          # в алерте считать х, найти результат функции и получить ответ - реализация степик
    time.sleep(5)

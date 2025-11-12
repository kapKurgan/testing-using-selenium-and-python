# pytest -v -s --tb=line --language=en test_product_page.py

from selenium.webdriver.common.by import By
from .pages.product_page import ProductPage
import time
from .pages.locators import ProductPageLocators                       # из файла locators.py импортируйте класс с локаторами ProductPageLocators

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)       # инициализировать Page Object, передать в конструктор экземпляр драйвера и url адрес
    page.open()                             # открыть страницу
    time.sleep(1)
    page.should_be_add_to_basket()          # проверить есть ли в карточке товара - Кнопка, цена, наименование товара
    page.product_add_to_basket()            # в карточке товара - цена, наименование товара
    page.press_add_to_basket_button()       # нажать кнопку "Добавить в корзину"
#    page.view_alert_math()                 # в алерте считать х, найти результат функции и получить ответ - реализация моя
    page.solve_quiz_and_get_code()          # в алерте считать х, найти результат функции и получить ответ - реализация степик
    page.should_product_in_basket()         # проверить есть ли в корзине - общая стоимость, наименование товара
    page.product_in_basket()                # в корзине - общая стоимость, наименование товара
    page.product_comparison()               # сравнить наименование и стоимость товара в карточке и корзине
    time.sleep(3)

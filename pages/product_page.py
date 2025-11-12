from selenium.common.exceptions import NoSuchElementException   # используется исключение для solve_quiz_and_get_code
from .locators import ProductPageLocators                       # из файла locators.py импортируйте класс с локаторами ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

class ProductPage(BasePage):
    def should_be_add_to_basket(self):
        # Проверить, что есть Кнопка - Добавить в корзину
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), ("Селектор 'ADD_TO_BASKET_BUTTON' Кнопка - Добавить в корзину не представлен")
        # Проверить, что есть Текст - Цена товара
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_PRICE), ("Селектор 'ADD_TO_BASKET_PRICE' Текст - Цена товара не представлен")
        # Проверить, что есть Текст - Наименование товара
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_NAME), ("Селектор 'ADD_TO_BASKET_NAME' Текст - Наименование товара не представлен")

    def should_product_in_basket(self):
        # Проверить, что есть В корзине - Наименование товара
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IN_BASKET_NAME), ("Селектор 'PRODUCT_IN_BASKET_NAME' В корзине - Наименование товара не представлен")
        # Проверить, что есть В корзине - Стоимость товара
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IN_BASKET_PRICE), ("Селектор 'PRODUCT_IN_BASKET_PRICE' В корзине - Стоимость товара не представлен")

    def product_add_to_basket(self):
        self.product_price = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_PRICE).text
        self.product_name = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_NAME).text

    def product_in_basket(self):
        self.basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_PRICE).text
        self.basket_name = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_NAME).text

    def product_comparison(self):
        print("##### В карточке - Наименование товара =", self.product_name)
        print("##### В корзине - Наименование товара =", self.basket_name)
        print("##### В карточке - Стоимость товара    =", self.product_price)
        print("##### В корзине - Стоимость товара    =", self.basket_price)
        assert self.product_name in self.basket_name, f"Наименование товара в карточке '{self.product_name}' и корзине '{self.basket_name}' НЕ СОВПАДАЮТ"
        assert self.product_price in self.basket_price, f"Стоимость товара в карточке '{self.product_price}' и корзине '{self.basket_price}' НЕ СОВПАДАЮТ"

    def press_add_to_basket_button(self):
        # Нажать кнопку Add to basket
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def view_alert_math(self):
        # в алерте считать х, найти результат функции и получить ответ - реализация моя
        alert_math = self.browser.switch_to.alert
        alert_text = alert_math.text
        x = int(alert_text.split()[2])
        y = calc(x)
        print("**************** x =", x, " *** y =", y)
        alert_math.send_keys(str(y))
        alert_math.accept()
        alert_result = self.browser.switch_to.alert
        alert_result_text = alert_result.text.split(': ')[-1]
        print("**************** alert_result_text =", alert_result_text)
        alert_result.accept()

    def solve_quiz_and_get_code(self):
        # в алерте считать х, найти результат функции и получить ответ - реализация stepik
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"***** Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("***** No second alert presented")



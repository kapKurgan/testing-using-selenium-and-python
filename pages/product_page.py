from selenium.common.exceptions import NoSuchElementException   # используется исключение для solve_quiz_and_get_code
from .locators import ProductPageLocators                       # из файла locators.py импортируйте класс с локаторами ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

class ProductPage(BasePage):
    def should_be_button_add_to_basket(self):
        # Проверить, что есть кнопка Add to basket
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), ("Селектор 'BUTTON_ADD_TO_BASKET' добавить в корзину не представлен")

    def press_button_add_to_basket(self):
        # Нажать кнопку Add to basket
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

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
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")



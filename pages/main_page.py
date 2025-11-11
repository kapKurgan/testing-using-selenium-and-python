# из файла locators.py импортируйте класс с локаторами
from .locators import MainPageLocators
from .base_page import BasePage
from .login_page import LoginPage

from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        # метод, который будет проверять наличие ссылки.
        # будем называть их should_be_(название элемента)
        # у *MainPageLocators.LOGIN_LINK символ *, он указывает на то, что мы передали именно пару, и этот кортеж
        # нужно распаковать
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Ссылка '#login_link' для входа в систему не представлена"


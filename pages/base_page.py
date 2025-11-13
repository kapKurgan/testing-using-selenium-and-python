from selenium.common.exceptions import NoSuchElementException  # используется методом is_element_present
from selenium.common.exceptions import TimeoutException  # используется методом is_element_present
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        # Конструктор класса.
        # browser -
        # url -
        # timeout - команда для неявного ожидания со значением по умолчанию в 10
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        # открыть нужную страницу, используя метод get()
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        # метод is_element_present, в котором будем перехватывать исключение. В него будем передавать два аргумента:
        # как искать (css, id, xpath и тд) и собственно что искать (строку-селектор)
        # NoSuchElementException - исключение
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        # метод, который проверяет, что элемент не появляется на странице в течение заданного времени
        # упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except (TimeoutException):
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        # Если хотим проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием вместе с функцией until_not
        # будет ждать до тех пор, пока элемент не исчезнет
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except (TimeoutException):
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Ссылка для входа в систему не представлена"

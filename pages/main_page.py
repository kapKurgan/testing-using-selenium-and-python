# из файла locators.py импортируйте класс с локаторами
from .locators import MainPageLocators
from .base_page import BasePage
from .login_page import LoginPage

from selenium.webdriver.common.by import By

class MainPage(BasePage):
    # Заглушка, можно просто pass
    def __init__(self, *args, **kwargs):
        # метод __init__ вызывается при создании объекта. Конструктор с ключевым словом super на самом деле только
        # вызывает конструктор класса предка и передает ему все те аргументы, которые передали в конструктор MainPage
        super(MainPage, self).__init__(*args, **kwargs)


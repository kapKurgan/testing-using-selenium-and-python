# из файла locators.py импортируйте класс с локаторами
from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        url = self.browser.current_url
        assert "login" in url, "url адрес "+url+" не содержит 'login'"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_EMAIL), ("Селектор 'LOGIN_INPUT_EMAIL' для входа в систему не представлен")
        assert self.is_element_present(*LoginPageLocators.LOGIN_INPUT_PASSWORD), ("Селектор 'LOGIN_INPUT_PASSWORD' для входа в систему не представлен")
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORGOT_PASSWORD), ("Селектор 'LOGIN_FORGOT_PASSWORD' для входа в систему не представлен")
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON_LOGIN), ("Селектор 'LOGIN_BUTTON_LOGIN' для входа в систему не представлен")

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_EMAIL), ("Селектор 'REGISTER_INPUT_EMAIL' для регистрации в систему не представлен")
        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_PASSWORD), ("Селектор 'REGISTER_INPUT_PASSWORD' для регистрации в систему не представлен")
        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_PASSWORD_CONFIRM), ("Селектор 'REGISTER_INPUT_PASSWORD_CONFIRM' для регистрации в систему не представлен")
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON_REGISTER), ("Селектор 'REGISTER_BUTTON_REGISTER' для регистрации в систему не представлен")

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_REGISTER).click()
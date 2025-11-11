from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

# селекторы к формам регистрации и логина
class LoginPageLocators():
    # Войти - Адрес электронной почты
    LOGIN_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    # Войти - Пароль
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    # Войти - Я забыл пароль
    LOGIN_FORGOT_PASSWORD = (By.CSS_SELECTOR, "#login_form > p > a")
    # Войти - Войти
    LOGIN_BUTTON_LOGIN = (By.CSS_SELECTOR, "button[name=login_submit]")

    # Зарегистрироваться - Адрес электронной почты
    REGISTER_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    # Зарегистрироваться - Пароль
    REGISTER_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    # Зарегистрироваться - Повторите пароль
    REGISTER_INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    # Зарегистрироваться - Зарегистрироваться
    REGISTER_BUTTON_REGISTER = (By.CSS_SELECTOR, "button[name=registration_submit]")

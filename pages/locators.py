from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

# селекторы к формам регистрации и логина http://selenium1py.pythonanywhere.com/ru/accounts/login/
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

class ProductPageLocators(object):
    # Кнопка - Добавить в корзину
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    # Текст - Цена товара
    ADD_TO_BASKET_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    # Текст - Наименование товара
    ADD_TO_BASKET_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    # В корзине - Наименование товара
    PRODUCT_IN_BASKET_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    # В корзине - Стоимость товара
    PRODUCT_IN_BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1)")
    #
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")

class BasePageLocators():
    # Кнопка - Войти или зарегистрироваться http://selenium1py.pythonanywhere.com/ru/
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # Кнопка - Войти или зарегистрироваться с несуществующим селектором
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    # Кнопка для перехода в корзину
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")        # "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a"
    #
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    # Если корзина не пуста, то по этому локатору будет находиться название товара в корзине, иначе этого селектора не будет
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, ".basket-items h3")
    # Плохой локатор, но другого нет. Если корзина не пуста,
    # то по этому локатору будут находится другие тексты, относящиеся к товару в корзине
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner p")  # "#content_inner > p"
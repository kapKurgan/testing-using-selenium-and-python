from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_message_about_empty_basket(self):
        # Ожидаем, что есть текст о том что корзина пуста
        text_about_empty_basket = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        assert text_about_empty_basket == "Your basket is empty. Continue shopping", ("Текст о пустой корзине отсутствует")

    def should_not_be_product_in_basket(self):
        # Ожидаем, что в корзине нет товаров
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_NAME), ("Название продукта указано, но не должно быть")
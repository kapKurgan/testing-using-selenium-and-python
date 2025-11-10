from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        # метод, который будет проверять наличие ссылки.
        # будем называть их should_be_(название элемента)
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Ссылка '#login_link' для входа в систему не представлена"
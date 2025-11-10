from selenium.common.exceptions import NoSuchElementException  # используется методом is_element_present

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

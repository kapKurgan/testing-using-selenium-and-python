# pytest -v -s --tb=line --language=en --alluredir=allure-results test_allure.py

# Allure-отчёт формируется в папке allure-results и запускается для просмотра командой:
# allure serve allure-results

# Чтобы запустить тесты с конкретным приоритетом:
# pytest tests/ --with-allure --logdir=tmp --severity="critical, hard"


# можно выгрузить Allure-отчёт, для передачи на компьютер без установленного Allure
# Отчёт будет сформирован в папку allure-report, которую можно передать на другой компьютер
# allure generate allure-results -o allure-report

# Открыть сформированный Allure-отчёт можно командой:
# allure open allure-report

# Сформированный Allure-отчёт можно запустить открыв файл index.html с помощью команды:
# start chrome --allow-file-access-from-files "C:/\<-You-Path-\>/allure-report/index.html"


from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import time
import pytest
import allure
from allure_commons.types import AttachmentType     # Отправка скриншота напрямую из драйвера
import random

TEST_CASE_LINK = 'https://github.com/kapKurgan/Selenium_Python_Final'


# Определяет задачу самого высокого уровня - корень дерева | меню Overview, Behaviors
@allure.epic("***** - @allure.epic - вкладка Behaviors (Поведение) -> Самый верх")
# Группирует тесты по проверяемому функционалу (функциональным блокам) | меню Behaviors
@allure.feature("***** - @allure.feature - Название модуля")
# Группирует тесты по User story. Помогает более детально описать функциональность, покрываемую тестом  | меню Behaviors
@allure.story("***** - @allure.story - История пользователя")
class TestAllurePageOne():
    # Задает наименование теста, которое будет отображаться в отчете. (Заменяет программное название тестовой функции) | раздел Description («Описание») тестового примера.
    @allure.title("***** - @allure.title - Название отчета 1/1")
    # В тесте, классе или модуле можно указать тэги тест-кейсов (тест-кейса) | страница/таб Overview («Обзор») теста
    @allure.tag("@allure.tag - Тэг 1")
    # Добавляет подробное описание теста, объясняя его цель и шаги | страница/таб Overview («Обзор»), раздел Description («Описание») тестового примера
    @allure.description("@allure.description - Добавляет описание (Description) к тесту")
    # или
    # @allure.description_html("@allure.description_html - Добавляет описание (Description) к тесту")
    # Указывает степень критичности теста | страница/таб Overview («Обзор») теста
    @allure.severity(allure.severity_level.CRITICAL)
    # Установит кликабельную ссылку на указанный URL-адрес в разделе Links «Ссылки» | страница/таб Overview («Обзор»), раздел Links («Ссылки») тестового примера
    @allure.link(TEST_CASE_LINK, name='Нажми меня')
    # Используется для ссылки на тест-кейсы в TMS (системах управления тестированием) | страница/таб Overview («Обзор»), раздел Links («Ссылки») тестового примера
    @allure.testcase(TEST_CASE_LINK, "TestCase-4215: Проверка входа в ЛК")
    # Установит ссылку с небольшим значком ошибки. Ссылается на задачи или баги в системах трекинга, таких как JIRA | страница/таб Overview («Обзор»), раздел Links («Ссылки») тестового примера
    @allure.issue(TEST_CASE_LINK, 'Повторные попытки теста Pytest-flaky показывают похожие шаги тестирования')
    # Помечает шаги теста, делая их видимыми в отчете. Может быть вложенной аннотацией внутри теста. Прописывается у метода/функции. В отчёте (при раскрытии шага) отображаются аргументы с которыми запускался метод/функция
    # | страница/таб Overview («Обзор») теста
    @allure.step("Шаг 1 - Открыть браузер")
    def test_allure_one_one(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        with allure.step(f'Шаг 2 - ссылка {link}'):
            page = MainPage(browser, link)                          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        with allure.step('Шаг 3 - открываем страницу'):
            page.open()                                             # открываем страницу
            # Отправка скриншота напрямую из драйвера
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

        page.go_to_login_page()                                 # выполняем метод страницы — переходим на страницу логина

        # Отправка скриншота напрямую из драйвера
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

        login_page = LoginPage(browser, browser.current_url)    # передаем объект драйвера для работы с
        # браузером, а в качестве url передаем текущий адрес
        login_page.should_be_login_page()                       # проверка на корректный url адрес
        # should_be_login_url из login_page.py

    @allure.title("***** - @allure.title - Название отчета 1/2")
    @allure.tag("@allure.tag - Тэг 2")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_allure_one_two(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

# Заменяет название пути от тестового каталога до файла с тестовом test_%name%.py | меню Overview, Suites
@allure.parent_suite("===== - @allure.parent_suite - вкладка Suites/Люксы (Группа тестов (suite)) -> Самый верх")
# Группирует тесты по Suite. Заменяет название файла test_%name%.py на вкладке Suites | меню Suites
@allure.suite("===== - @allure.suite - вкладка Suites/Люксы")
# Заменяет название тестового класса, который находится в  test_%name%.py | меню Suites
@allure.sub_suite("===== - @allure.sub_suite - вкладка Suites/Люксы")
class TestAllurePageTwo():
#    @allure.title("===== - @allure.title - Название отчета 2/1")
    @allure.tag("@allure.tag - Тэг 3")
    @allure.severity(allure.severity_level.MINOR)
    def test_allure_two_one(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)                          # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                                             # открываем страницу
        page.go_to_login_page()                                 # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)    # передаем объект драйвера для работы с
        # браузером, а в качестве url передаем текущий адрес
        login_page.should_be_login_page()                       # проверка на корректный url адрес
        # should_be_login_url из login_page.py

#    @allure.title("===== - @allure.title - Название отчета 2/2")
    @allure.tag("@allure.tag - Тэг 4")
    @allure.severity(allure.severity_level.NORMAL)
    def test_allure_two_two(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.parametrize("input_value", ["1", "2", "3", "4", "5", "6"])
def test_dynamic_metadata(input_value):
    # Генерируем случайные данные для демонстрации
    test_case_id = random.randint(1000, 9999)
    priority = random.choice(["HIGH", "MEDIUM", "LOW"])

    # Устанавливаем динамические метаданные
    allure.dynamic.title(f"Тест #TC-{test_case_id}")
    allure.dynamic.description(f"""
    Автоматически сгенерированный тест.
    Приоритет: {priority}
    ID тест-кейса: TC-{test_case_id}-{input_value}
    """)

    if priority == "HIGH":
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.dynamic.tag("smoke")
    else:
        allure.dynamic.severity(allure.severity_level.NORMAL)

    # Тестовый код
    assert True
import pytest
from selenium import webdriver


# Добавление опций в командную строку
def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help="Choose language: es, fr, de, etc.")

    parser.addoption('--browser',
                     action='store',
                     default='chrome',
                     choices=['chrome', 'firefox', 'edge'],
                     help="Choose browser: chrome, firefox, edge")


# Фикстура для инициализации разных браузеров
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser").lower()
    language = request.config.getoption("language")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", language)
        driver = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        driver = webdriver.Edge(options=options)

    else:
        raise pytest.UsageError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit()


# Фикстура для получения выбранного языка
@pytest.fixture
def language(request):
    return request.config.getoption("language")
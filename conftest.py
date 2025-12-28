import pytest
import os
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language")
    parser.addoption('--browser', action='store', default='chrome',
                     choices=['chrome', 'firefox', 'edge'], help="Choose browser")
    parser.addoption('--headless', action='store_true', help="Run in headless mode")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser").lower()
    language = request.config.getoption("language")
    headless = request.config.getoption("headless") or os.getenv('CI')  # Авто-включение в CI

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("intl.accept_languages", language)
        if headless:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")  # Для CI
        driver = webdriver.Firefox(options=options)

    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Edge(options=options)

    yield driver
    driver.quit()


@pytest.fixture
def language(request):
    return request.config.getoption("language")
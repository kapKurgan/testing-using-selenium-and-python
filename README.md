# Автоматизация тестирования с помощью Selenium и Python

## Как запускать тесты

Чтобы запустить любой тестовый файл, используйте следующую команду:

```bash
pytest -v --tb=line --language=en ИМЯ_ФАЙЛА.py
```

Если вы проверяете этот проект, пожалуйста, используйте следующую команду для запуска ключевых тестов, отмеченных @pytest.mark.need_review:

```bash
pytest -v --tb=line --language=en -m need_review
```

## Примечания
Если у вас возникли проблемы с запуском моего теста, попробуйте изменить пути импорта, версию pytest и selenium.

# Allure для Python (автоматизация тестирования)

## Как запускать тесты

Чтобы запустить тестовый файл, используйте следующую команду:

```bash
pytest -v -s --tb=line --language=en --alluredir=allure-results test_allure.py
```

Отчет формируется в папке allure-results и запускается для просмотра командой:

```bash
allure serve allure-results
```

![alt tag](https://github.com/kapKurgan/Selenium_Python_Final/blob/main/github_pict/allure_1.png)

![alt tag](https://github.com/kapKurgan/Selenium_Python_Final/blob/main/github_pict/allure_2.png)

![alt tag](https://github.com/kapKurgan/Selenium_Python_Final/blob/main/github_pict/allure_3.png)

![alt tag](https://github.com/kapKurgan/Selenium_Python_Final/blob/main/github_pict/allure_4.png)

![alt tag](https://github.com/kapKurgan/Selenium_Python_Final/blob/main/github_pict/allure_5.png)

![alt tag](https://github.com/kapKurgan/Selenium_Python_Final/blob/main/github_pict/allure_6.png)


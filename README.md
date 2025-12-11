# Web Autotest SauceDemo

Проект автоматизированного тестирования веб-приложения SauceDemo с использованием Playwright и pytest.

## Структура проекта

```
web-autotest-saucedemo/
├── conftest.py              # Конфигурация pytest и фикстуры
├── pytest.ini               # Настройки pytest и Allure
├── requirements.txt         # Зависимости проекта
├── data/                    # Тестовые данные
│   ├── users.py            # Пользователи для тестирования
│   └── error_messag.py     # Сообщения об ошибках
├── locators/                # Локаторы элементов
│   ├── login_locator.py
│   ├── burger_menu_locator.py
│   └── catalog_locator.py
├── pages/                    # Page Object Model
│   ├── main_page.py
│   ├── login_page.py
│   ├── burger_menu_page.py
│   └── catalog_page.py
└── tests/                    # Тесты
    └── ui/
        ├── test_login.py
        └── test_product_catalog_and_Inventory.py
```

## Запуск автотестов на Windows

1. Активируйте виртуальное окружение:
```bash
venv\Scripts\activate
```

2. Запустите все тесты:
```bash
pytest
```

3. Запуск с Allure отчетом:

   **Вариант 1** (если allure в PATH):
   ```bash
   pytest --alluredir=allure-results
   allure serve allure-results
   ```

   **Вариант 2** (с указанием полного пути до allure):
   ```bash
   pytest --alluredir=allure-results
   абсолютный путь да allure.bat serve allure-results
   ```

   Для поиска пути к allure выполните:
   ```bash
   where allure.bat
   ```
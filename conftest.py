import pytest
import allure

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.burger_menu_page import PrimerWindowPage
from pages.catalog_page import CatalogPage
from data.users import Users

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args): # Настройки для контекста браузера
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
        "java_script_enabled": True,
        "has_touch": False,
        "locale": "ru-RU",
        "timezone_id": "Europe/Moscow",
    }

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call): #Хук для создания скриншотов при ошибках тестов
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        for fixture_name in item.fixturenames:
            if 'page' in fixture_name or 'login_page' in fixture_name or 'burger_menu_page' in fixture_name:
                try:
                    page_obj = item.funcargs.get(fixture_name)
                    if page_obj and hasattr(page_obj, 'page'):
                        screenshot = page_obj.page.screenshot()
                        allure.attach(
                            screenshot,
                            name="screenshot",
                            attachment_type=allure.attachment_type.PNG
                        )
                        break
                except Exception as e:
                    print(f"Не удалось сделать скриншот: {e}")


@pytest.fixture(scope="function")
def login_page(page): #Фикстура для страницы логина без авторизации
    with allure.step("Инициализация страницы логина"):
        login_page = LoginPage(page)
        login_page.navigate("")
        return login_page


@pytest.fixture(scope="function")
def authorized_login_page(login_page):
    with allure.step(f"Авторизация пользователя {Users.STANDARD_USER.username}"):
        login_page.login(
            Users.STANDARD_USER.username,
            Users.STANDARD_USER.password)
        return login_page


@pytest.fixture(scope="function")
def authorized_burger_menu_page(authorized_login_page):
    with allure.step("Инициализация бургер-меню для авторизованного пользователя"):
        burger_menu_page = PrimerWindowPage(authorized_login_page.page)
        return burger_menu_page

@pytest.fixture(scope="function")
def authorized_catalog_page(authorized_login_page):
    with allure.step("Инициализация бургер-меню для авторизованного пользователя"):
        catalog_page = CatalogPage(authorized_login_page.page)
        return catalog_page

@pytest.fixture(scope="function")
def authorized_and_add_4_item_page(authorized_login_page):
    with allure.step("Инициализация страницы каталога для авторизованного пользователя"):
        catalog_page = CatalogPage(authorized_login_page.page)
    for i in range(4):
        with allure.step(f"Добавление {i} товара в корзину"):
            catalog_page.click_add_to_cart_by_index(i)
    with allure.step("Переход на страницу корзины"):
        catalog_page.click_cart_link()
    with allure.step("Инициализация страницы корзины"):
        basket_page = BasketPage(catalog_page.page)
        return basket_page

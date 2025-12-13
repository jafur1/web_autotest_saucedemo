import pytest
import allure
from pages.login_page import LoginPage
from pages.burger_menu_page import PrimerWindowPage
from pages.catalog_page import CatalogPage
from data.users import Users


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
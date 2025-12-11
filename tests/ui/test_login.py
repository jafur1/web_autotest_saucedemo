from data.users import *
from data.error_messag import *
import pytest
import allure


@allure.epic("Авторизация")
@allure.feature("Логин")
class TestLogin:
    @allure.story("Успешная авторизация")
    @allure.title("Вход с валидными учетными данными стандартного пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_valid_user_login(self, login_page):
        with allure.step(f"Ввод логина: {Users.STANDARD_USER.username}"):
            login_page.enter_login_input(Users.STANDARD_USER.username)
        with allure.step("Ввод пароля"):
            login_page.enter_password_input(Users.STANDARD_USER.password)
        with allure.step("Нажатие кнопки входа"):
            login_page.click_login_button()
        with allure.step("Проверка успешной авторизации"):
            assert login_page.is_logged_in(), "Пользователь не авторизован"

    @allure.story("Неуспешная авторизация")
    @allure.title("Вход с неверным паролем")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_invalid_login(self, login_page):
        with allure.step(f"Ввод логина: {Users.STANDARD_INCORRECT_PASSWORD_USER.username}"):
            login_page.enter_login_input(Users.STANDARD_INCORRECT_PASSWORD_USER.username)
        with allure.step("Ввод неверного пароля"):
            login_page.enter_password_input(Users.STANDARD_INCORRECT_PASSWORD_USER.password)
        with allure.step("Нажатие кнопки входа"):
            login_page.click_login_button()
        with allure.step("Проверка сообщения об ошибке"):
            error_message = login_page.error_text()
            assert error_message == LoginErrorMessage.STANDARD_INVALID_MESSAGE, \
                f"Ожидалось: {LoginErrorMessage.STANDARD_INVALID_MESSAGE}, получено: {error_message}"

    @allure.story("Блокировка пользователя")
    @allure.title("Вход заблокированного пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    def test_blocked_user_login(self, login_page):
        with allure.step(f"Ввод логина заблокированного пользователя: {Users.LOCKED_OUT_USER.username}"):
            login_page.enter_login_input(Users.LOCKED_OUT_USER.username)
        with allure.step("Ввод пароля"):
            login_page.enter_password_input(Users.LOCKED_OUT_USER.password)
        with allure.step("Нажатие кнопки входа"):
            login_page.click_login_button()
        with allure.step("Проверка сообщения о блокировке"):
            error_message = login_page.error_text()
            assert error_message == LoginErrorMessage.LOCKED_OUT_USER, \
                f"Ожидалось: {LoginErrorMessage.LOCKED_OUT_USER}, получено: {error_message}"

    @allure.story("Проблемный пользователь")
    @allure.title("Вход проблемного пользователя")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    def test_problem_user_login(self, login_page):
        with allure.step(f"Ввод логина проблемного пользователя: {Users.PROBLEM_USER.username}"):
            login_page.enter_login_input(Users.PROBLEM_USER.username)
        with allure.step("Ввод пароля"):
            login_page.enter_password_input(Users.PROBLEM_USER.password)
        with allure.step("Нажатие кнопки входа"):
            login_page.click_login_button()
        with allure.step("Проверка успешной авторизации"):
            assert login_page.is_logged_in(), "Проблемный пользователь не авторизован"

    @allure.story("Выход из системы")
    @allure.title("Выход из системы авторизованного пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_logout(self, authorized_burger_menu_page, authorized_login_page):
        with allure.step("Проверка, что пользователь авторизован"):
            assert authorized_login_page.is_logged_in(), "Пользователь не авторизован"
        with allure.step("Выполнение выхода из системы через бургер-меню"):
            authorized_burger_menu_page.click_logout()
        with allure.step("Проверка успешного выхода из системы"):
            assert authorized_login_page.is_logout_in(), "Выход из системы не выполнен"

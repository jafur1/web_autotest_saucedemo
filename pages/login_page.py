from pages.main_page import MainPage
from locators.login_locator import LoginLocator

class LoginPage(MainPage):
    @property
    def login_input(self):
        return self.page.locator(LoginLocator.USERNAME_INPUT_LOCATOR)
    @property
    def password_input(self):
        return self.page.locator(LoginLocator.PASSWORD_INPUT_LOCATOR)
    @property
    def login_button(self):
        return self.page.locator(LoginLocator.LOGIN_BUTTON_LOCATOR)
    @property
    def error_message(self):
        return self.page.locator(LoginLocator.ERROR_MESSAGE_LOCATOR)

    def enter_login_input(self,username):  # Ввести логин в поле ввода
        self.login_input.fill(username)

    def enter_password_input(self,password):  # Ввести пароль в поле ввода
        self.password_input.fill(password)

    def click_login_button(self):  # Нажать кнопку входа
        self.login_button.click()

    def login(self, username, password):  # Выполнить полный процесс авторизации
        self.enter_login_input(username)
        self.enter_password_input(password)
        self.click_login_button()
        self.page.wait_for_load_state("networkidle")

    def error_text(self) -> str:  # Получить текст сообщения об ошибке
        return self.error_message.text_content()

    def is_logged_in(self) -> bool:  # Проверить, авторизован ли пользователь
        return "/inventory.html" in self.page.url

    def is_logout_in(self) -> bool:  # Проверить, выполнен ли выход из системы
        return  not "/inventory.html" in self.page.url
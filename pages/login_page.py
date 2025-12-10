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

    def enter_login_input(self,username):
        self.login_input.fill(username)

    def enter_password_input(self,password):
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def login(self, username, password):
        self.enter_login_input(username)
        self.enter_password_input(password)
        self.click_login_button()
        # Ждем навигации после логина (либо на inventory.html, либо остаемся на странице логина с ошибкой)
        self.page.wait_for_load_state("networkidle")

    def error_text(self) -> str:
        return self.error_message.text_content()

    def is_logged_in(self) -> bool:
        """Проверяет, залогинен ли пользователь, проверяя URL после логина"""
        # После успешного логина URL должен содержать /inventory.html
        return "/inventory.html" in self.page.url
from playwright.sync_api import Page


class MainPage:
    def __init__(self, page: Page):  # Инициализация базовой страницы
        self.page = page
        self.main_url = "https://www.saucedemo.com/"

    def navigate(self, url: str):  # Перейти на указанный URL
        if "http://" in url or "https://" in url:
            self.page.goto(self.main_url)
        else:
            target_url = self.main_url + url
            self.page.goto(target_url)
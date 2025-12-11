from pages.main_page import MainPage
from locators.burger_menu_locator import BurgerMenuLocator

class PrimerWindowPage(MainPage):
    @property
    def burger_menu_locator(self):
        return self.page.locator(BurgerMenuLocator.OPEN_BURGER_MENU_BUTTON)
    @property
    def logout_locator(self):
        return self.page.locator(BurgerMenuLocator.LOGOUT_BUTTON)
    @property
    def about_locator(self):
        return self.page.locator(BurgerMenuLocator.ABOUT_BUTTON)
    @property
    def reset_app_state_locator(self):
        return self.page.locator(BurgerMenuLocator.RESET_APP_STATE_BUTTON)
    @property
    def all_items_locator(self):
        return self.page.locator(BurgerMenuLocator.ALL_ITEMS_BUTTON)

    def open_burger_menu(self):
        self.burger_menu_locator.click()
    def click_logout(self):
        self.open_burger_menu()
        self.logout_locator.click()
    def click_all_items(self):
        self.open_burger_menu()
        self.all_items_locator.click()
    def click_reset_app_state(self):
        self.open_burger_menu()
        self.reset_app_state_locator.click()
    def click_about(self):
        self.open_burger_menu()
        self.about_locator.click()





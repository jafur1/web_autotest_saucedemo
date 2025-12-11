from locators.catalog_locator import CatalogLocator
from pages.main_page import MainPage

class CatalogPage(MainPage):
    @property
    def table_product_locator(self):
        return self.page.locator(CatalogLocator.TABLE_PRODUCT_CARDS)
    @property
    def card_locator(self):
        return self.page.locator(CatalogLocator.CARD_LOCATOR)
    @property
    def add_cart_locator(self):
        return self.page.locator(CatalogLocator.ADD_CART_BUTTON)
    @property
    def remove_cart_locator(self):
        return self.page.locator(CatalogLocator.REMOVE_BUTTON)
    @property
    def open_filter_locator(self):
        return self.page.locator(CatalogLocator.OPEN_FILTER_BUTTON)
    @property
    def sort_a_to_z(self):
        return self.page.locator(CatalogLocator.SORT_A_TO_Z)
    @property
    def sort_z_to_a(self):
        return self.page.locator(CatalogLocator.SORT_Z_TO_A)
    @property
    def sort_low_to_high(self):
        return self.page.locator(CatalogLocator.SORT_LOW_TO_HIGH)
    @property
    def sort_high_to_low(self):
        return self.page.locator(CatalogLocator.SORT_HIGH_TO_LOW)
    @property
    def cart_title_locator(self):
        return self.page.locator(CatalogLocator.CART_TITLE)

# дописать функции для работы с картами товаров

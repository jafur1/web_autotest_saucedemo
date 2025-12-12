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
    def sort_a_to_z_locator(self):
        return self.page.locator(CatalogLocator.SORT_A_TO_Z)
    @property
    def sort_z_to_a_locator(self):
        return self.page.locator(CatalogLocator.SORT_Z_TO_A)
    @property
    def sort_low_to_high_locator(self):
        return self.page.locator(CatalogLocator.SORT_LOW_TO_HIGH)
    @property
    def sort_high_to_low_locator(self):
        return self.page.locator(CatalogLocator.SORT_HIGH_TO_LOW)
    @property
    def cart_title_locator(self):
        return self.page.locator(CatalogLocator.CART_TITLE)

    def get_product_cards_count(self) -> int:  # Получить количество карточек товаров на странице
        return self.card_locator.count()

    def get_product_card_by_index(self, index: int):  # Получить карточку товара по индексу
        return self.card_locator.nth(index)

    def get_product_name_by_index(self, index: int) -> str:  # Получить название товара по индексу
        card = self.get_product_card_by_index(index)
        return card.locator(CatalogLocator.CART_TITLE).text_content()

    def get_product_price_by_index(self, index: int) -> str:  # Получить цену товара по индексу
        card = self.get_product_card_by_index(index)
        price_locator = card.locator('.inventory_item_price')
        return price_locator.text_content()

    def click_add_to_cart_by_index(self, index: int):  # Добавить товар в корзину по индексу
        card = self.get_product_card_by_index(index)
        add_button = card.locator('button[data-test*="add-to-cart"]')
        add_button.click()

    def click_remove_from_cart_by_index(self, index: int):  # Удалить товар из корзины по индексу
        card = self.get_product_card_by_index(index)
        remove_button = card.locator('button[data-test*="remove"]')
        remove_button.click()

    def click_product_card_by_index(self, index: int):  # Кликнуть по карточке товара по индексу (переход на страницу товара)
        card = self.get_product_card_by_index(index)
        card.locator(CatalogLocator.CART_TITLE).click()

    def click_add_to_cart_by_name(self, product_name: str):  # Добавить товар в корзину по названию
        count = self.get_product_cards_count()
        for i in range(count):
            if self.get_product_name_by_index(i) == product_name:
                self.click_add_to_cart_by_index(i)
                break

    def click_remove_from_cart_by_name(self, product_name: str):  # Удалить товар из корзины по названию
        count = self.get_product_cards_count()
        for i in range(count):
            if self.get_product_name_by_index(i) == product_name:
                self.click_remove_from_cart_by_index(i)
                break

    def get_all_product_names(self) -> list:  # Получить список всех названий товаров на странице
        names = []
        count = self.get_product_cards_count()
        for i in range(count):
            names.append(self.get_product_name_by_index(i))
        return names

    def get_all_product_prices(self) -> list:  # Получить список всех цен товаров на странице
        prices = []
        count = self.get_product_cards_count()
        for i in range(count):
            prices.append(self.get_product_price_by_index(i))
        return prices

    def is_product_in_cart_by_index(self, index: int) -> bool:  # Проверить, добавлен ли товар в корзину по индексу
        card = self.get_product_card_by_index(index)
        remove_button = card.locator('button[data-test*="remove"]')
        return remove_button.is_visible()

    def click_sort_a_to_z(self):  # Сортировать товары от A до Z
        self.open_filter_locator.click()
        self.sort_a_to_z_locator.click()
        self.page.wait_for_load_state("networkidle")

    def click_sort_z_to_a(self):  # Сортировать товары от Z до A
        self.open_filter_locator.click()
        self.sort_z_to_a_locator.click()
        self.page.wait_for_load_state("networkidle")

    def click_sort_low_to_high(self):  # Сортировать товары по цене от низкой к высокой
        self.open_filter_locator.click()
        self.sort_low_to_high_locator.click()
        self.page.wait_for_load_state("networkidle")

    def click_sort_high_to_low(self):  # Сортировать товары по цене от высокой к низкой
        self.open_filter_locator.click()
        self.sort_high_to_low_locator.click()
        self.page.wait_for_load_state("networkidle")

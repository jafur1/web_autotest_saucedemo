from locators.basket_locator import BasketLocator
from pages.main_page import MainPage

class BasketPage(MainPage):
    @property
    def remove_button_locator(self):
        return self.page.locator(BasketLocator.REMOVE_BUTTON)
    @property
    def checkout_locator(self):
        return self.page.locator(BasketLocator.CHECKOUT_BUTTON)
    @property
    def continue_shopping_button_locator(self):
        return self.page.locator(BasketLocator.CONTINUE_SHOPPING_BUTTON)
    @property
    def item_basket_locator(self):
        return self.page.locator(BasketLocator.ITEM_BASKET_LOCATOR)

    def count_item_basket(self) -> int: # Подсчёт количества добавленных товаров
        return self.item_basket_locator.count()

    def delete_item(self, item_id: int): # Удаление элемента по индексу
        return self.remove_button_locator.click()[item_id]
# Реализовать пейджи для корзины
from playwright.sync_api import expect
import allure
import pytest


@allure.epic("Каталог товаров")
@allure.feature("Отображение и сортировка товаров")
class TestCatalog:

    @allure.story("Отображение каталога")
    @allure.title("Проверка отображения каталога товаров")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_display_product_catalog(self, authorized_catalog_page):
        with allure.step("Проверка видимости карточек товаров"):
            expect(authorized_catalog_page.cards_locator).to_be_visible()
        with allure.step("Проверка количества товаров в каталоге"):
            assert authorized_catalog_page.get_product_cards_count() == 6, \
                f"Ожидалось 6 товаров, получено {authorized_catalog_page.get_product_cards_count()}"

    @allure.story("Сортировка товаров")
    @allure.title("Сортировка товаров от Z до A")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_sort_z_to_a(self, authorized_catalog_page):
        with allure.step("Получение списка имен товаров до сортировки"):
            names_before = authorized_catalog_page.get_all_product_names()
        with allure.step("Создание ожидаемого списка, отсортированного от Z до A"):
            expected_names = sorted(names_before, reverse=True)
        with allure.step("Применение сортировки Z to A"):
            authorized_catalog_page.click_sort_z_to_a()
        with allure.step("Получение списка имен товаров после сортировки"):
            names_after = authorized_catalog_page.get_all_product_names()
        with allure.step("Проверка корректности сортировки"):
            assert names_after == expected_names, f"Ожидалось {expected_names}, получено {names_after}"

    @allure.story("Сортировка товаров")
    @allure.title("Сортировка товаров по цене от низкой к высокой")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_sort_low_to_high(self, authorized_catalog_page):
        with allure.step("Получение списка цен товаров до сортировки"):
            prase_before = authorized_catalog_page.get_all_product_prices()
        with allure.step("Применение сортировки от низкой к высокой"):
            authorized_catalog_page.click_sort_low_to_high()
        with allure.step("Получение списка цен товаров после сортировки"):
            prase_after = authorized_catalog_page.get_all_product_prices()
        with allure.step("Проверка изменения порядка товаров"):
            assert prase_before != prase_after, f"Кнопка сортировки не работает"

    @allure.story("Сортировка товаров")
    @allure.title("Сортировка товаров по цене от высокой к низкой")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_sort_high_to_low(self, authorized_catalog_page):
        with allure.step("Получение списка цен товаров до сортировки"):
            prase_before = authorized_catalog_page.get_all_product_prices()
        with allure.step("Применение сортировки от высокой к низкой"):
            authorized_catalog_page.click_sort_high_to_low()
        with allure.step("Получение списка цен товаров после сортировки"):
            prase_after = authorized_catalog_page.get_all_product_prices()
        with allure.step("Проверка изменения порядка товаров"):
            assert prase_before != prase_after, f"Кнопка сортировки не работает"

# реализовать class TestBasket:
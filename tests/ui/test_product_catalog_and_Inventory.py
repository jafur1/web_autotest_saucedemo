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

@allure.epic("Работа с корзиной из окна каталога товаров")
@allure.feature("Добавление и удаление товаров без перехода в корзину")
class TestAddAndDeleteBasket:

    @allure.story("Работа с добавление и удаление товаров")
    @allure.title("Добавление 1 товара в корзину")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_add_1_item_to_basket(self, authorized_catalog_page):
        with allure.step("Добавление товара с индексом 1"):
            authorized_catalog_page.click_add_to_cart_by_index(1)
        with allure.step("Получение количества добавленных товаров в корзину и запись в переменную"):
            item = authorized_catalog_page.count_item_basket()
        with allure.step("Сравнение ранее созданной переменной с актуальным значением количества товаров в корзине"):
            assert item == 1, f"Был добавлен один товар, а корзина посчитала {item}"

    @allure.story("Работа с добавление и удаление товаров")
    @allure.title("Добавление 3 товара в корзину")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    @pytest.mark.regression
    def test_add_3_item_to_basket(self, authorized_catalog_page):
        with allure.step("Добавление первого товара с индексом 1"):
            authorized_catalog_page.click_add_to_cart_by_index(1)
        with allure.step("Получение имени второго товара"):
            name_2_item = authorized_catalog_page.get_product_name_by_index(2)
        with allure.step("Получение имени третьего товара"):
            name_3_item = authorized_catalog_page.get_product_name_by_index(3)
        with allure.step("Добавление второго товара по имени"):
            authorized_catalog_page.click_add_to_cart_by_name(name_2_item)
        with allure.step("Добавление третьего товара по имени"):
            authorized_catalog_page.click_add_to_cart_by_name(name_3_item)
        with allure.step("Получение количества добавленных товаров в корзину"):
            item = authorized_catalog_page.count_item_basket()
        with allure.step("Проверка количества товаров в корзине"):
            assert item == 3, f"Было добавлено 3 товара, а корзина посчитала {item}"

    @allure.story("Работа с добавление и удаление товаров")
    @allure.title("Добавление 2 товара в корзину и удаление 1 товара из корзины")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    @pytest.mark.smoke
    def test_delete_item_basket(self, authorized_catalog_page):
        with allure.step("Добавление первого товара с индексом 1"):
            authorized_catalog_page.click_add_to_cart_by_index(1)
        with allure.step("Добавление второго товара с индексом 2"):
            authorized_catalog_page.click_add_to_cart_by_index(2)
        with allure.step("Получение количества добавленных товаров в корзину"):
            item = authorized_catalog_page.count_item_basket()
        with allure.step("Проверка количества товаров в корзине после добавления"):
            assert item == 2, f"Было добавлено 2 товара, а корзина посчитала {item}"
        with allure.step("Удаление первого товара из корзины"):
            authorized_catalog_page.click_remove_from_cart_by_index(1)
        with allure.step("Получение количества товаров в корзине после удаления"):
            item_new = authorized_catalog_page.count_item_basket()
        with allure.step("Проверка количества товаров в корзине после удаления"):
            assert item_new == 1, f"Было добавлено 2 товара и 1 товар удалён , а корзина посчитала {item_new}"




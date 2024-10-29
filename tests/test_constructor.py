import pytest
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage
import allure

@allure.suite("Проверка основного функционала")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_navigate_to_constructor(self, browser_setup):
        page = ConstructorPage(self.driver)
        page.go_to_constructor()

        assert page.is_constructor_page(), "Не удалось перейти в раздел 'Конструктор'"

    @allure.title("Переход по клику на «Лента заказов»")
    def test_navigate_to_order_feed(self, browser_setup):
        page = ConstructorPage(self.driver)
        page.go_to_order_feed()

        assert page.is_order_feed_page(), "Не удалось перейти в раздел 'Лента заказов'"

    @allure.title("Появление и закрытие всплывающего окна с деталями ингредиента")
    def test_ingredient_modal_window(self, browser_setup):
        page = ConstructorPage(self.driver)
        page.go_to_constructor()
        page.open_ingredient_details()

        assert page.is_ingredient_modal_open(), "Всплывающее окно с деталями ингредиента не открылось"

        page.close_ingredient_modal()

        assert page.is_ingredient_modal_closed(), "Всплывающее окно с деталями ингредиента не закрылось"

    @allure.title("Проверка увеличения каунтера ингредиента после добавления")
    def test_ingredient_counter_increase(self, browser_setup):
        page = ConstructorPage(self.driver)
        page.go_to_constructor()
        page.go_to_sauces_section()
        initial_count = page.get_galactic_sauce_counter()
        page.drag_and_drop_ingredient_to_constructor()
        page.wait_for_condition(lambda: page.get_galactic_sauce_counter() == initial_count + 1, timeout=10)
        updated_count = page.get_galactic_sauce_counter()

        assert updated_count == initial_count + 1, "Каунтер ингредиента не увеличился"

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_place_order(self, browser_setup, create_user):
        page = ConstructorPage(self.driver)
        login_page = LoginPage(self.driver)
        login_page.login_via_web(create_user["email"], create_user["password"])
        page.drag_and_drop_ingredient_to_constructor()
        page.place_order()

        assert page.is_order_successful(), "Не удалось оформить заказ"

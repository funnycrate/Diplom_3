import allure
from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from pages.constructor_page import ConstructorPage

@allure.suite("Проверка 'Ленты заказов'")
class TestOrderFeed:

    @allure.title("Открытие всплывающего окна с деталями заказа при клике на заказ")
    def test_order_details_modal(self, browser_setup):
        page = FeedPage(self.driver)
        page.go_to_order_feed()
        page.open_order_details()

        assert page.is_order_modal_open(), "Всплывающее окно с деталями заказа не открылось"

    @allure.title("Заказы пользователя отображаются в 'Ленте заказов'")
    def test_user_orders_display_in_feed(self, browser_setup, create_user):
        page = FeedPage(self.driver)
        constructor_page = ConstructorPage(self.driver)
        personal_account = PersonalAccountPage(self.driver)
        login_account = LoginPage(self.driver)
        page.go_to_account()
        login_account.login_via_web(create_user["email"], create_user["password"])
        constructor_page.place_order_for_user()
        page.close_order_modal()
        page.go_to_account()
        personal_account.go_to_order_history()
        order_id_from_history = page.get_last_order_id_from_history()
        order_id_from_feed = page.get_last_order_id_from_feed()

        assert order_id_from_history == order_id_from_feed, "Заказ пользователя не отображается в ленте заказов"

    @allure.title("Проверка увеличения счётчика 'Выполнено за всё время'")
    def test_total_orders_completed_counter(self, browser_setup, create_user):
        page = FeedPage(self.driver)
        constructor_page = ConstructorPage(self.driver)
        login_account = LoginPage(self.driver)
        page.go_to_order_feed()
        initial_total = page.get_total_orders_completed()
        page.go_to_account()
        login_account.login_via_web(create_user["email"], create_user["password"])
        constructor_page.place_order_for_user()
        page.close_order_modal()
        page.go_to_order_feed()
        new_total = page.get_total_orders_completed()

        assert new_total == initial_total + 1, "Счётчик 'Выполнено за всё время' не увеличился"

    @allure.title("Проверка увеличения счётчика 'Выполнено за сегодня'")
    def test_today_orders_completed_counter(self, browser_setup, create_user):
        page = FeedPage(self.driver)
        constructor_page = ConstructorPage(self.driver)
        login_account = LoginPage(self.driver)
        page.go_to_order_feed()
        initial_today = page.get_today_orders_completed()
        page.go_to_account()
        login_account.login_via_web(create_user["email"], create_user["password"])
        constructor_page.place_order_for_user()
        page.close_order_modal()
        page.go_to_order_feed()
        new_today = page.get_today_orders_completed()

        assert new_today == initial_today + 1, "Счётчик 'Выполнено за сегодня' не увеличился"

    @allure.title("Номер нового заказа отображается в разделе 'В работе'")
    def test_in_progress_order_number_displayed(self, browser_setup, create_user):
        page = FeedPage(self.driver)
        login_account = LoginPage(self.driver)
        constructor_page = ConstructorPage(self.driver)
        login_account.login_via_web(create_user["email"], create_user["password"])
        constructor_page.place_order_for_user()
        page.close_order_modal()
        page.go_to_order_feed()
        order_number = page.get_in_progress_order_number()

        assert order_number, "Номер нового заказа не отображается в разделе 'В работе'"
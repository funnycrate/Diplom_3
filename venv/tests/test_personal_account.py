import pytest
from data import Urls
from pages.personal_account_page import PersonalAccountPage
import allure

@allure.suite("Тесты личного кабинета")
class TestAccount:

    @allure.title("Переход в личный кабинет по кнопке 'Личный Кабинет'")
    def test_navigate_to_account(self, browser_setup, create_user):
        account_page = PersonalAccountPage(self.driver)
        account_page.login_via_web(create_user["email"], create_user["password"])  # Логин через веб
        account_page.go_to_account()
        assert account_page.is_account_page(), "Не удалось перейти в личный кабинет"

    @allure.title("Переход в раздел 'История заказов'")
    def test_navigate_to_order_history(self, browser_setup, create_user):
        account_page = PersonalAccountPage(self.driver)
        account_page.login_via_web(create_user["email"], create_user["password"])  # Логин через веб
        account_page.go_to_account()
        account_page.go_to_order_history()
        assert account_page.get_current_url() == Urls.ORDER_HISTORY_URL, "Не удалось перейти в раздел 'История заказов'"

    @allure.title("Выход из аккаунта")
    def test_logout_from_account(self, browser_setup, create_user):
        account_page = PersonalAccountPage(self.driver)
        account_page.login_via_web(create_user["email"], create_user["password"])  # Логин через веб
        account_page.go_to_account()
        account_page.logout()
        assert account_page.get_current_url() == Urls.LOGIN_URL, "Не удалось выйти из аккаунта"
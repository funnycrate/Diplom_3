import pytest
from data import Urls
from pages.recovery_page import RecoveryPage
from pages.login_page import LoginPage
import allure

@allure.suite("Тесты восстановления пароля")
class TestRecoveryPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке")
    def test_navigate_to_recovery_page(self, browser_setup):
        login_page = LoginPage(self.driver)
        login_page.go_to_recovery_page()

        assert login_page.get_current_url() == Urls.FORGOT_PASS_URL, "Не удалось перейти на страницу восстановления пароля"

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_recovery_email_submission(self, browser_setup):
        recovery_page = RecoveryPage(self.driver)
        login_page = LoginPage(self.driver)
        login_page.go_to_recovery_page()
        recovery_page.input_recovery_email("test@example.com")
        recovery_page.click_recovery_button()

        assert recovery_page.get_current_url() == Urls.RESET_PASS_URL, "Не удалось перейти на страницу восстановления пароля"

    @allure.title("Клик по кнопке показать/скрыть пароль активирует поле")
    def test_toggle_password_visibility(self, browser_setup):
        recovery_page = RecoveryPage(self.driver)
        login_page = LoginPage(self.driver)
        login_page.go_to_recovery_page()
        recovery_page.input_recovery_email("test@example.com") 
        recovery_page.click_recovery_button()

        assert recovery_page.is_password_field_inactive(), "Поле пароля должно быть неактивным до клика 'Показать пароль'"

        recovery_page.toggle_password_visibility()

        assert recovery_page.is_password_field_active(), "Поле пароля не стало активным при показе пароля"

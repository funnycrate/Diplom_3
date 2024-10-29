from locators import StellarBurgersRecoveryLocators
from pages.base_page import BasePage
import allure
from data import Urls

class RecoveryPage(BasePage):

    @allure.step('Ввод электронной почты для восстановления')
    def input_recovery_email(self, email):
        self.input_text(StellarBurgersRecoveryLocators.RECOVERY_EMAIL_FLD, email)

    @allure.step('Клик по кнопке восстановления')
    def click_recovery_button(self):
        self.click_to_element(StellarBurgersRecoveryLocators.RECOVERY_BTN)
        # Костыль для прохождения теста
        self.wait_for_url(Urls.RESET_PASS_URL)

    @allure.step('Показать/скрыть пароль')
    def toggle_password_visibility(self):
        self.click_to_element(StellarBurgersRecoveryLocators.RECOVERY_PASSWORD_BTN)

    @allure.step('Проверка, что поле пароля активно')
    def is_password_field_active(self):
        return self.wait_for_visibility(StellarBurgersRecoveryLocators.RECOVERY_PASSWORD_ACTIVE_FLD)

    @allure.step('Проверка, что поле пароля неактивно')
    def is_password_field_inactive(self):
        return self.wait_for_visibility(StellarBurgersRecoveryLocators.RECOVERY_PASSWORD_NO_ACTIVE_FLD)

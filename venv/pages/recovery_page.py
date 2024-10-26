from locators import StellarBurgersRecoveryLocators, StellarBurgersLoginLocators
from pages.base_page import *
import allure
from data import Urls

class RecoveryPage(BasePage):

    @allure.step('Переход на страницу восстановления пароля')
    def go_to_recovery_page(self):
        self.click_to_element(StellarBurgersLoginLocators.FORGOT_PASS_LNK)

    @allure.step('Ввод электронной почты для восстановления')
    def input_recovery_email(self, email):
        self.input_text(StellarBurgersRecoveryLocators.RECOVERY_EMAIL_FLD, email)

    @allure.step('Клик по кнопке восстановления')
    def click_recovery_button(self):
        self.click_to_element(StellarBurgersRecoveryLocators.RECOVERY_BTN)
        # Костыль для прохождения теста
        WebDriverWait(self.driver, 10).until(EC.url_to_be(Urls.RESET_PASS_URL))

    @allure.step('Показать/скрыть пароль')
    def toggle_password_visibility(self):
        self.click_to_element(StellarBurgersRecoveryLocators.RECOVERY_PASSWORD_BTN)

    @allure.step('Проверка, что поле пароля активно')
    def is_password_field_active(self):
        return self.wait_element(StellarBurgersRecoveryLocators.RECOVERY_PASSWORD_ACTIVE_FLD)

    @allure.step('Проверка, что поле пароля неактивно')
    def is_password_field_inactive(self):
        return self.wait_element(StellarBurgersRecoveryLocators.RECOVERY_PASSWORD_NO_ACTIVE_FLD)

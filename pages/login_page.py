from locators import StellarBurgersLoginLocators
from pages.base_page import BasePage
import allure

class LoginPage(BasePage):

    @allure.step("Переход на страницу восстановления пароля")
    def go_to_recovery_page(self):
        self.click_to_element(StellarBurgersLoginLocators.FORGOT_PASS_LNK)

    @allure.step('Вход в личный кабинет через веб-интерфейс')
    def login_via_web(self, email, password):
        self.input_text(StellarBurgersLoginLocators.LOGIN_EMAIL_FLD, email)
        self.input_text(StellarBurgersLoginLocators.LOGIN_PASS_FLD, password)
        self.click_to_element(StellarBurgersLoginLocators.LOGIN_SUBMIT_BTN)
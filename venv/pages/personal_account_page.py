from pages.base_page import BasePage
from data import Urls
from locators import *
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PersonalAccountPage(BasePage):

    @allure.step('Переход в личный кабинет')
    def go_to_account(self):
        self.click_to_element(StellarBurgersBaseLocators.ACC_BTN)

    @allure.step('Проверка URL личного кабинета')
    def is_account_page(self):
        current_url = self.get_current_url()
        assert current_url == Urls.ACCOUNT_URL, f"Ожидался URL {Urls.ACCOUNT_URL}, но загружен {current_url}"
        return current_url == Urls.ACCOUNT_URL

    @allure.step('Вход в личный кабинет через веб-интерфейс')
    def login_via_web(self, email, password):
        self.input_text(StellarBurgersLoginLocators.LOGIN_EMAIL_FLD, email)
        self.input_text(StellarBurgersLoginLocators.LOGIN_PASS_FLD, password)
        self.click_to_element(StellarBurgersLoginLocators.LOGIN_SUBMIT_BTN)

    @allure.step('Переход в раздел "История заказов"')
    def go_to_order_history(self):
        self.click_to_element(StellarBurgersPersonalAccountLocators.HISTORY_OF_ORDERS_BTN)

    @allure.step('Выход из аккаунта')
    def logout(self):
        self.click_to_element(StellarBurgersPersonalAccountLocators.LOGOUT_FROM_ACC_BTN)
        # Костыль для прохождения теста
        WebDriverWait(self.driver, 10).until(EC.url_to_be(Urls.LOGIN_URL))
        current_url = self.get_current_url()
        assert current_url == Urls.LOGIN_URL, f"Ожидался URL {Urls.LOGIN_URL}, но загружен {current_url}"
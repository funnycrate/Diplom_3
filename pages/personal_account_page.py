from pages.base_page import BasePage
from data import Urls
from locators import StellarBurgersPersonalAccountLocators
import allure

class PersonalAccountPage(BasePage):

    @allure.step('Проверка, что пользователь на странице личного кабинета')
    def is_account_page(self):
        current_url = self.get_current_url()
        return current_url == Urls.ACCOUNT_URL

    @allure.step('Переход в раздел "История заказов"')
    def go_to_order_history(self):
        self.click_to_element(StellarBurgersPersonalAccountLocators.HISTORY_OF_ORDERS_BTN)

    @allure.step('Выход из аккаунта')
    def logout(self):
        self.click_to_element(StellarBurgersPersonalAccountLocators.LOGOUT_FROM_ACC_BTN)
        self.wait_for_url(Urls.LOGIN_URL)


from pages.base_page import BasePage
from locators import StellarburgersFeedLocators
import allure
import re


class FeedPage(BasePage):

    @allure.step("Клик по заказу для открытия деталей")
    def open_order_details(self):
        self.click_to_element(StellarburgersFeedLocators.ORDER_ITEM)

    @allure.step("Проверка открытия всплывающего окна с деталями заказа")
    def is_order_modal_open(self):
        self.wait_for_presence(StellarburgersFeedLocators.ORDER_MODAL, timeout=10)
        return True

    @allure.step("Получение количества выполненных заказов за всё время")
    def get_total_orders_completed(self):
        total_orders_element = self.wait_for_visibility(StellarburgersFeedLocators.TOTAL_ORDERS_COMPLETED)
        return int(total_orders_element.text)

    @allure.step("Получение количества выполненных заказов за сегодня")
    def get_today_orders_completed(self):
        today_orders_element = self.wait_for_visibility(StellarburgersFeedLocators.TODAY_ORDERS_COMPLETED)
        return int(today_orders_element.text)

    @allure.step("Проверка номера последнего заказа в разделе 'В работе'")
    def get_in_progress_order_number(self):
        order_number_element = self.wait_for_visibility(StellarburgersFeedLocators.IN_PROGRESS_ORDER_NUMBER)
        return order_number_element.text

    @allure.step("Получение идентификатора последнего заказа из 'Истории заказов'")
    def get_last_order_id_from_history(self):
        order_text = self.get_element_text(StellarburgersFeedLocators.ORDER_ITEM)
        return re.search(r'#(\d+)', order_text).group(1)

    @allure.step("Получение идентификатора последнего заказа из 'Ленты заказов'")
    def get_last_order_id_from_feed(self):
        self.go_to_order_feed()
        order_text = self.get_element_text(
            StellarburgersFeedLocators.ORDER_ITEM)
        return re.search(r'#(\d+)', order_text).group(1)

    @allure.step("Закрытие окна успешного создания заказа")
    def close_order_modal(self):
        self.close_modal(StellarburgersFeedLocators.ORDER_MODAL_CLOSE)

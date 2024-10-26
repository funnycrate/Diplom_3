from pages.base_page import BasePage
from locators import *
from pages.personal_account_page import PersonalAccountPage
from pages.constructor_page import ConstructorPage
from selenium.webdriver.common.action_chains import ActionChains
import allure
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class FeedPage(BasePage):

    @allure.step("Переход в раздел 'Лента заказов'")
    def go_to_order_feed(self):
        self.click_to_element(StellarBurgersBaseLocators.LST_ORD)

    @allure.step("Оформление заказа для пользователя")
    def place_order_for_user(self, email, password):
        account_page = PersonalAccountPage(self.driver)
        account_page.login_via_web(email, password)
        self.drag_and_drop_to_constructor(StellarBurgersConstructorLocators.CRATER_BREAD_ICON)  # Используем обобщенный метод
        ConstructorPage(self.driver).place_order()

    @allure.step("Клик по заказу для открытия деталей")
    def open_order_details(self):
        self.click_to_element(StellarburgersFeedLocators.ORDER_ITEM)

    @allure.step("Проверка открытия всплывающего окна с деталями заказа")
    def is_order_modal_open(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(StellarburgersFeedLocators.ORDER_MODAL)
        )
        return True

    @allure.step("Получение количества выполненных заказов за всё время")
    def get_total_orders_completed(self):
        total_orders_element = self.wait_element(StellarburgersFeedLocators.TOTAL_ORDERS_COMPLETED)
        return int(total_orders_element.text)

    @allure.step("Получение количества выполненных заказов за сегодня")
    def get_today_orders_completed(self):
        today_orders_element = self.wait_element(StellarburgersFeedLocators.TODAY_ORDERS_COMPLETED)
        return int(today_orders_element.text)

    @allure.step("Проверка номера последнего заказа в разделе 'В работе'")
    def get_in_progress_order_number(self):
        order_number_element = self.wait_element(StellarburgersFeedLocators.IN_PROGRESS_ORDER_NUMBER)
        return order_number_element.text

    @allure.step("Переход в 'Историю заказов' из личного кабинета")
    def go_to_order_history(self):
        self.go_to_personal_account()
        self.click_to_element(StellarBurgersPersonalAccountLocators.HISTORY_OF_ORDERS_BTN)

    @allure.step("Получение идентификатора последнего заказа из 'Истории заказов'")
    def get_last_order_id_from_history(self):
        self.go_to_order_history()
        order_text = self.get_text_locator(StellarburgersFeedLocators.ORDER_ITEM)
        return re.search(r'#(\d+)', order_text).group(1)

    @allure.step("Получение идентификатора последнего заказа из 'Ленты заказов'")
    def get_last_order_id_from_feed(self):
        self.go_to_order_feed()
        order_text = self.get_text_locator(StellarburgersFeedLocators.ORDER_ITEM)
        return re.search(r'#(\d+)', order_text).group(1)

    @allure.step("Закрытие окна успешного создания заказа")
    def close_order_modal(self):
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
        try:
            WebDriverWait(self.driver, 10).until_not(
                EC.presence_of_element_located((By.CLASS_NAME, "Modal_modal_opened__3ISw4"))
            )
        except TimeoutException:
            raise AssertionError("Модальное окно успешного заказа не исчезло")

    @allure.step('Перетаскивание ингредиента в конструктор')
    def drag_and_drop_to_constructor(self, ingredient_locator):
        ingredient = self.wait_element(ingredient_locator)
        drop_zone = self.wait_element(StellarBurgersConstructorLocators.DROP_ZONE)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, drop_zone).perform()

    @allure.step("Переход в 'Личный кабинет'")
    def go_to_personal_account(self):
        self.close_order_modal()  #
        self.click_to_element(StellarBurgersBaseLocators.ACC_BTN)
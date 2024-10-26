from pages.base_page import BasePage
from locators import StellarBurgersBaseLocators, StellarBurgersConstructorLocators
from selenium.webdriver import ActionChains
from data import Urls
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
import time

class ConstructorPage(BasePage):

    @allure.step('Переход в раздел "Конструктор"')
    def go_to_constructor(self):
        self.click_to_element(StellarBurgersBaseLocators.CONSTR_BTN)

    @allure.step('Проверка URL раздела "Конструктор"')
    def is_constructor_page(self):
        current_url = self.get_current_url()
        assert current_url == Urls.BASE_URL, f"Ожидался URL {Urls.BASE_URL}, но загружен {current_url}"
        return current_url == Urls.BASE_URL

    @allure.step('Переход в раздел "Лента заказов"')
    def go_to_order_feed(self):
        self.click_to_element(StellarBurgersBaseLocators.LST_ORD)

    @allure.step('Проверка URL раздела "Лента заказов"')
    def is_order_feed_page(self):
        current_url = self.get_current_url()
        assert current_url == Urls.ORDER_FEED_URL, f"Ожидался URL {Urls.ORDER_FEED_URL}, но загружен {current_url}"
        return current_url == Urls.ORDER_FEED_URL

    @allure.step('Переход в раздел "Соусы"')
    def go_to_sauces_section(self):
        self.click_to_element(StellarBurgersConstructorLocators.SAUCES_LIST)

    @allure.step('Открытие всплывающего окна с деталями ингредиента')
    def open_ingredient_details(self):
        self.go_to_sauces_section()
        self.click_to_element(StellarBurgersConstructorLocators.GALACTIC_SAUCE_ICON)

    @allure.step('Проверка открытия всплывающего окна ингредиента')
    def is_ingredient_modal_open(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(StellarBurgersConstructorLocators.INGREDIENT_MODAL_OPENED)
        )
        return True

    @allure.step('Проверка закрытия всплывающего окна ингредиента')
    def is_ingredient_modal_closed(self):
        WebDriverWait(self.driver, 10).until_not(
            EC.presence_of_element_located(StellarBurgersConstructorLocators.INGREDIENT_MODAL_OPENED)
        )
        return True

    @allure.step('Закрытие всплывающего окна с деталями ингредиента')
    def close_ingredient_modal(self):
        self.click_to_element(StellarBurgersConstructorLocators.CLOSE_INGR_WINDOW_BTN)

    @allure.step("Получение значения каунтера галактического соуса")
    def get_galactic_sauce_counter(self):
        galactic_sauce_counter = self.driver.find_element(*StellarBurgersConstructorLocators.GALACTIC_SAUCE_COUNTER)
        return int(galactic_sauce_counter.text)

    @allure.step('Перетаскивание ингредиента в конструктор')
    def drag_and_drop_ingredient_to_constructor(self):
        ingredient = self.wait_element(StellarBurgersConstructorLocators.GALACTIC_SAUCE_ICON)
        drop_zone = self.wait_element(StellarBurgersConstructorLocators.DROP_ZONE)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, drop_zone).perform()

    @allure.step('Оформление заказа')
    def place_order(self):
        self.click_to_element(StellarBurgersConstructorLocators.PLACE_ORDER_BTN)

    @allure.step('Проверка успешного оформления заказа')
    def is_order_successful(self):
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(StellarBurgersConstructorLocators.ORDER_SUCCESS_MESSAGE)
        )
        return success_message.is_displayed()

from pages.base_page import BasePage
from locators import StellarBurgersConstructorLocators
from selenium.webdriver import ActionChains
from data import Urls
import allure

class ConstructorPage(BasePage):

    @allure.step('Проверка, что URL соответствует разделу "Конструктор"')
    def is_constructor_page(self):
        return self.get_current_url() == Urls.BASE_URL

    @allure.step('Проверка URL раздела "Лента заказов"')
    def is_order_feed_page(self):
        return self.get_current_url() == Urls.ORDER_FEED_URL

    @allure.step('Переход в раздел "Соусы"')
    def go_to_sauces_section(self):
        self.click_to_element(StellarBurgersConstructorLocators.SAUCES_LIST)

    @allure.step('Открытие всплывающего окна с деталями ингредиента')
    def open_ingredient_details(self):
        self.go_to_sauces_section()
        self.click_to_element(StellarBurgersConstructorLocators.GALACTIC_SAUCE_ICON)

    @allure.step('Проверка открытия всплывающего окна ингредиента')
    def is_ingredient_modal_open(self):
        return self.is_element_visible(StellarBurgersConstructorLocators.INGREDIENT_MODAL_OPENED)

    @allure.step('Проверка закрытия всплывающего окна ингредиента')
    def is_ingredient_modal_closed(self):
        return not self.is_element_visible(StellarBurgersConstructorLocators.INGREDIENT_MODAL_OPENED)

    @allure.step('Закрытие всплывающего окна с деталями ингредиента')
    def close_ingredient_modal(self):
        self.click_to_element(StellarBurgersConstructorLocators.CLOSE_INGR_WINDOW_BTN)

    @allure.step("Получение значения каунтера галактического соуса")
    def get_galactic_sauce_counter(self):
        counter_text = self.get_element_text(StellarBurgersConstructorLocators.GALACTIC_SAUCE_COUNTER)
        return int(counter_text)

    @allure.step('Перетаскивание ингредиента в конструктор')
    def drag_and_drop_ingredient_to_constructor(self):
        ingredient = self.wait_for_visibility(StellarBurgersConstructorLocators.GALACTIC_SAUCE_ICON)
        drop_zone = self.wait_for_visibility(StellarBurgersConstructorLocators.DROP_ZONE)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, drop_zone).perform()

    @allure.step('Клик по оформлению заказа')
    def place_order(self):
        self.click_to_element(StellarBurgersConstructorLocators.PLACE_ORDER_BTN)

    @allure.step('Проверка успешного оформления заказа')
    def is_order_successful(self):
        return self.is_element_visible(StellarBurgersConstructorLocators.ORDER_SUCCESS_MESSAGE)

    @allure.step("Оформление заказа для пользователя")
    def place_order_for_user(self):
        self.drag_and_drop_bread_to_constructor(StellarBurgersConstructorLocators.CRATER_BREAD_ICON)
        self.place_order()

    @allure.step('Перетаскивание ингредиента в конструктор')
    def drag_and_drop_bread_to_constructor(self, ingredient_locator):
        ingredient = self.wait_for_visibility(ingredient_locator)
        drop_zone = self.wait_for_visibility(StellarBurgersConstructorLocators.DROP_ZONE)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(ingredient, drop_zone).perform()

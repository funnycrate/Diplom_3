from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from locators import StellarBurgersBaseLocators
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание присутствия элемента {locator}')
    def wait_for_presence(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Ожидание видимости элемента {locator}')
    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Поиск элемента {locator}')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Получение текста элемента {locator}')
    def get_element_text(self, locator):
        element = self.wait_for_visibility(locator)
        return element.text

    @allure.step('Клик по элементу {locator}')
    def click_to_element(self, locator):
        element = self.wait_for_visibility(locator)
        element.click()

    @allure.step('Ввод текста "{text}" в элемент {locator}')
    def input_text(self, locator, text):
        element = self.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Прокрутка до элемента {locator}')
    def scroll_to_element(self, locator):
        element = self.wait_for_visibility(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переход на страницу входа')
    def go_to_login_page(self):
        self.click_to_element(StellarBurgersBaseLocators.ACC_BTN)  # кнопка "Личный Кабинет" или "Вход"

    @allure.step("Проверка видимости элемента")
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Ожидание, что элемент {locator} станет невидимым")
    def wait_for_invisibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Отправка клавиши "{keys}" в элемент {locator}')
    def send_keys_to_element(self, locator, keys):
        element = self.wait_for_visibility(locator)
        element.send_keys(keys)

    @allure.step("Ожидание, что URL станет {url}")
    def wait_for_url(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    @allure.step('Переход в раздел "Конструктор"')
    def go_to_constructor(self):
        self.click_to_element(StellarBurgersBaseLocators.CONSTR_BTN)

    @allure.step('Переход в раздел "Лента заказов"')
    def go_to_order_feed(self):
        self.click_to_element(StellarBurgersBaseLocators.LST_ORD)

    @allure.step('Переход в личный кабинет')
    def go_to_account(self):
        self.click_to_element(StellarBurgersBaseLocators.ACC_BTN)

    @allure.step("Закрытие модального окна")
    def close_modal(self, locator, timeout=10):
        """Закрывает модальное окно, отправляя клавишу ESCAPE, и ожидает, пока оно исчезнет."""
        self.send_keys_to_element((By.TAG_NAME, 'body'), Keys.ESCAPE)
        if not self.wait_for_invisibility(locator, timeout=10):
            raise AssertionError("Модальное окно не исчезло")

    @allure.step("Ожидание выполнения условия")
    def wait_for_condition(self, condition_function, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: condition_function())
            return True
        except TimeoutException:
            return False
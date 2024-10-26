from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common.exceptions import TimeoutException
from locators import *

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание видимости элемента {locator}')
    def wait_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Клик по элементу {locator}')
    def click_to_element(self, locator):
        element = self.wait_element(locator)
        element.click()

    @allure.step('Ввод текста "{text}" в элемент {locator}')
    def input_text(self, locator, text):
        element = self.wait_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Прокрутка до элемента {locator}')
    def scroll_to_element(self, locator):
        element = self.wait_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получение текста из элемента {locator}')
    def get_text_locator(self, locator):
        element = self.wait_element(locator)
        return element.text

    @allure.step('Переход на новую вкладку с URL {url}')
    def go_to_new_tab(self, url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    @allure.step('Переход на страницу входа')
    def go_to_login_page(self):
        self.click_to_element(StellarBurgersBaseLocators.ACC_BTN)  # кнопка "Личный Кабинет" или "Вход"

    @allure.step("Проверка видимости элемента")
    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
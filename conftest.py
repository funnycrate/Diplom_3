import pytest
import json
import requests
from browser_factory import BrowserFactory
from helpers import generate_user_data
from pages.base_page import BasePage
from data import Urls


# Чтение доступных браузеров из config/browsers.json
with open("config/browsers.json") as f:
    browsers = json.load(f)["browsers"]

@pytest.fixture(scope="function", params=browsers)
def browser_setup(request):
    browser = request.param
    driver = BrowserFactory.get_driver(browser)
    driver.maximize_window()
    driver.get(Urls.BASE_URL) 
    base_page = BasePage(driver)
    base_page.go_to_login_page()  
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(scope="function")
def get_user_token():
    """Получение токена для авторизованного пользователя."""
    def _get_token(email, password):
        url = f"{Urls.API_URL}/auth/login"
        response = requests.post(url, json={"email": email, "password": password})
        token = response.json().get("accessToken")
        return token
    return _get_token

@pytest.fixture(scope="function")
def create_user(get_user_token):
    """Создает уникального пользователя перед тестом и удаляет его после."""
    user_data = generate_user_data()

    # Регистрация нового пользователя
    url = f"{Urls.API_URL}/auth/register"
    response = requests.post(url, json=user_data)

    yield user_data

    # Удаление пользователя после теста
    token = get_user_token(user_data["email"], user_data["password"])
    delete_url = f"{Urls.API_URL}/auth/user"
    headers = {'Authorization': token}
    delete_response = requests.delete(delete_url, headers=headers)


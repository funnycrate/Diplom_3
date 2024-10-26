from faker import Faker
from datetime import datetime


fake = Faker()
class Urls:
    # Адрес главной страницы
    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    # Адрес для работы с API
    API_URL = "https://stellarburgers.nomoreparties.site/api"
    # Адрес для ввода почты на экране восстановления пароля
    FORGOT_PASS_URL = "https://stellarburgers.nomoreparties.site/forgot-password"
    # Адрес экрана восстановления пароля
    RESET_PASS_URL = "https://stellarburgers.nomoreparties.site/reset-password"
    # Адрес экрана личного кабинета
    ACCOUNT_URL = "https://stellarburgers.nomoreparties.site/account"
    # Адрес экрана истории заказов
    ORDER_HISTORY_URL = "https://stellarburgers.nomoreparties.site/account/order-history"
    # Адрес экрана логина
    LOGIN_URL = "https://stellarburgers.nomoreparties.site/login"
    # Адрес экрана "Лента заказов"
    ORDER_FEED_URL = "https://stellarburgers.nomoreparties.site/feed"

def generate_user_data():
    """Генерирует данные пользователя с уникальным email и статичным паролем."""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    unique_email = f"{fake.user_name()}_{timestamp}@example.com"
    return {
        "email": unique_email,
        "password": "12345678",  # Оставляем фиксированный пароль
        "name": fake.first_name()
    }
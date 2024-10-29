class Urls:
    # Адрес главной страницы
    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    # Адрес для работы с API
    API_URL = f"{BASE_URL}api"
    # Адрес для ввода почты на экране восстановления пароля
    FORGOT_PASS_URL = f"{BASE_URL}forgot-password"
    # Адрес экрана восстановления пароля
    RESET_PASS_URL = f"{BASE_URL}reset-password"
    # Адрес экрана личного кабинета
    ACCOUNT_URL = f"{BASE_URL}account"
    # Адрес экрана истории заказов
    ORDER_HISTORY_URL = f"{BASE_URL}account/order-history"
    # Адрес экрана логина
    LOGIN_URL = f"{BASE_URL}login"
    # Адрес экрана "Лента заказов"
    ORDER_FEED_URL = f"{BASE_URL}feed"
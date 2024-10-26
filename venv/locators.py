from selenium.webdriver.common.by import By

class StellarBurgersBaseLocators:
    # кнопка "Личный Кабинет"
    ACC_BTN = (By.LINK_TEXT, "Личный Кабинет")

    # Лого "СтелларБургерс"
    LOGO = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']")

    # Кнопка "Конструктор"
    CONSTR_BTN = (By.XPATH, "//a[@class = 'AppHeader_header__link__3D_hX']")

    #Кнопка "Лента заказов"
    LST_ORD = (By.XPATH, ".//p[text()='Лента Заказов']")

class StellarBurgersRecoveryLocators:
    # Кнопка "Восстановить" в окне восстановления пароля
    RECOVERY_BTN = (By.XPATH, "//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

    # Поле ввода электронной почты в окне восстановлении пароля
    RECOVERY_EMAIL_FLD = (By.XPATH, "//input[@class = 'text input__textfield text_type_main-default']")

    # Поле ввода пароля в окне восстановления пароля (неактивное)
    RECOVERY_PASSWORD_NO_ACTIVE_FLD = (By.XPATH, "//label[@class = 'input__placeholder text noselect text_type_main-default']")

    # Кнопка "Показать пароль" в окне восстановления пароля
    RECOVERY_PASSWORD_BTN = (By.XPATH, "//div[@class = 'input__icon input__icon-action']")

    # Поле ввода пароля в окне восстановления пароля (активное)
    RECOVERY_PASSWORD_ACTIVE_FLD = (By.XPATH, "//label[@class = 'input__placeholder text noselect text_type_main-default input__placeholder-focused']")

class StellarBurgersLoginLocators:
    # кнопка "Зарегистрироваться" в окне входа
    REG_LNK = (By.LINK_TEXT, "Зарегистрироваться")

    # Поле ввода электронной почты в окне входа
    LOGIN_EMAIL_FLD = (By.XPATH, ".//input[@name = 'name']")

    # Поле ввода пароля в окне входа
    LOGIN_PASS_FLD = (By.XPATH, ".//input[@name = 'Пароль']")

    # Кнопка "Войти" в окне входа
    LOGIN_SUBMIT_BTN = (By.XPATH, ".//button[contains(text(), 'Войти')]")

    # Кнопка "Восстановить пароль" в окне входа
    FORGOT_PASS_LNK = (By.LINK_TEXT, "Восстановить пароль")

class StellarBurgersPersonalAccountLocators:
    # Кнопка "История заказов" в личном кабинете
    HISTORY_OF_ORDERS_BTN = (By.XPATH, "//a[@class = 'Account_link__2ETsJ text text_type_main-medium text_color_inactive']")

    # Кнопка "Выход" в личном кабинете
    LOGOUT_FROM_ACC_BTN = (By.XPATH, "//button[@class= 'Account_button__14Yp3 text text_type_main-medium text_color_inactive']")

class StellarBurgersConstructorLocators:

    # Кнопка "Оформить заказ" в личном кабинете
    PLACE_ORDER_BTN = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")

    # Кнопка выхода из личного кабинета
    LOGOUT_BTN = (By.XPATH, ".//button[contains(text(), 'Выход')]")

    # Раздел "Соусы" в конструкторе бургеров
    SAUCES_LIST = (By.XPATH, ".//h2[contains(text(), 'Соусы')]")

    # Иконка галактического соуса
    GALACTIC_SAUCE_ICON = (By.XPATH, ".//img[@alt = 'Соус традиционный галактический']")

    # Раздел "Начинки" в конструкторе бургеров
    TOPPINGS_LIST = (By.XPATH, ".//h2[contains(text(), 'Начинки')]")

    # Иконка выбора говяжьего метеорита
    BEAF_METEOR_ICON = (By.XPATH, ".//img[@alt = 'Говяжий метеорит (отбивная)']")

    # Раздел "Булки" в конструкторе бургеров
    BREAD_LIST = (By.XPATH, ".//h2[contains(text(), 'Булки')]")

    # Иконка выбора краторной булки
    CRATER_BREAD_ICON = (By.XPATH, "//img[@alt='Краторная булка N-200i']")

    # Калории в окне галактического соуса
    GALACTIC_SAUCE_CAL = (By.XPATH, ".//p[contains(text(), '99')]")

    # Калории в окне говяжьего метеорита
    BEAF_METEOR_CAL = (By.XPATH, ".//p[contains(text(), '2674')]")

    # Калории в окне краторной булки
    CRATER_BREAD_CAL = (By.XPATH, ".//p[contains(text(), '420')]")

    # Кнопка "Закрыть" всплывающего окна ингредиента
    CLOSE_INGR_WINDOW_BTN = (By.XPATH, "//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")

    # Каунтер ингредиента "Соус традиционный галактический"
    GALACTIC_SAUCE_COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter__ZNLkj') and following-sibling::p[text()='Соус традиционный галактический']]//p[@class='counter_counter__num__3nue1']")

    INGREDIENT_MODAL_OPENED = (By.CLASS_NAME, "Modal_modal_opened__3ISw4")

    INGREDIENT_MODAL_CLOSED = (By.CLASS_NAME, "Modal_modal__P3_V5")

    # Зона для сброса ингредиентов в конструкторе
    DROP_ZONE = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")

    # Сообщение об успешном оформлении заказа
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//p[contains(@class, 'text_type_main-small') and contains(text(), 'Ваш заказ начали готовить')]")


class StellarburgersFeedLocators:
    # Локатор для отдельного заказа, по которому можно кликнуть
    ORDER_ITEM = (By.CSS_SELECTOR, "a.OrderHistory_link__1iNby")

    # Всплывающее окно с деталями заказа
    ORDER_MODAL = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")

    # Счётчик выполненных заказов за всё время
    TOTAL_ORDERS_COMPLETED = (By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p")

    # Счётчик выполненных заказов за сегодня
    TODAY_ORDERS_COMPLETED = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p")

    # Локатор для номера заказа в "Истории заказов" и "Ленте заказов"
    ORDER_NUMBER = (By.CSS_SELECTOR, "div.OrderHistory_textBox__3lgbs p.text_type_digits-default")

    # Раздел "В работе" с номером последнего заказа
    IN_PROGRESS_ORDER_NUMBER = (By.CSS_SELECTOR, ".OrderFeed_orderList__cBvyi li.text_type_digits-default")

    ORDER_MODAL_CLOSE = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS")

    ORDER_MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
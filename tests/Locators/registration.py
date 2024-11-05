class Registration:
    """Локаторы для страницы регистрации"""
    # Кнопка "Далее" на форме регистрации
    SUBMIT_BTN = '[data-wi=submit-button][data-pw=auth-widget-signup-form]'
    # Алерт поля "Имя пользователя"
    USERNAME_ALERT = '[data-wi="user-name"] [role="alert"]'
    # Алерт поля "Электронная почта"
    EMAIL_ALERT = '[data-wi="identificator"] [role="alert"]'
    # Алерт поля "Пароль"
    PASSWORD_ALERT = '[data-wi="password"] [role="alert"]'
    # Чек-бокс user-agreement
    USER_AGREEMENT_CHECKBOX = '[data-wi="user-agreement"] [role="checkbox"]'
    # Поле ввода "Имя пользователя"
    USERNAME_INPUT = '[data-wi="user-name"]'
    # Поле ввода "Электронная почта"
    EMAIL_INPUT = '[data-wi="identificator"]'
    # Поле ввода "Пароль"
    PASSWORD_INPUT = '[data-wi="password"]'

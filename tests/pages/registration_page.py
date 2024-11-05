from playwright.sync_api import Page

from tests.locators.registration import Registration
from tests.pages.base import Base
from tests.tests.enums import REGISTRATION_URL, EMPTY_FIELD_ALERT, RED, SHORT_PASSWORD_ALERT


class RegistrationPage(Base):
    """Методы для страницы регистрации"""

    def __init__(self, page: Page):
        super().__init__(page)

    def goto(self):
        """Открывает страницу регистрации"""
        self.open(REGISTRATION_URL)

    def click_submit_button(self):
        """Отмечает чек-бокс согласия с Условиями использования"""
        self.click(Registration.SUBMIT_BTN)

    def check_empty_user_name_alert(self):
        """Проверяет текст и цвет"""
        self.element_has_text(Registration.USERNAME_ALERT, EMPTY_FIELD_ALERT)
        self.element_has_color(Registration.USERNAME_ALERT, RED)

    def check_empty_email_alert(self):
        """Проверяет текст и цвет"""
        self.element_has_text(Registration.EMAIL_ALERT, EMPTY_FIELD_ALERT)
        self.element_has_color(Registration.EMAIL_ALERT, RED)

    def check_empty_password_alert(self):
        """Проверяет текст и цвет"""
        self.element_has_text(Registration.PASSWORD_ALERT, EMPTY_FIELD_ALERT)
        self.element_has_color(Registration.USERNAME_ALERT, RED)

    def check_short_password_alert(self):
        """Проверяет текст и цвет"""
        self.element_has_text(Registration.PASSWORD_ALERT, SHORT_PASSWORD_ALERT)
        self.element_has_color(Registration.PASSWORD_ALERT, RED)

    def click_user_agreement_checkbox(self):
        """Нажимает чек-бокс Согласие с пользовательским соглашением"""
        self.click(Registration.USER_AGREEMENT_CHECKBOX)

    def input_username_field(self, username):
        """Нажимает на поле Имя пользователя и вводит текст"""
        self.click(Registration.USERNAME_INPUT)
        self.input(Registration.USERNAME_INPUT, username)

    def input_email_field(self, email):
        """Нажимает на поле Электронная почта и вводит текст"""
        self.click(Registration.EMAIL_INPUT)
        self.input(Registration.EMAIL_INPUT, email)

    def input_password_field(self, password):
        """Нажимает на поле Пароль и вводит текст"""
        self.click(Registration.PASSWORD_INPUT)
        self.input(Registration.PASSWORD_INPUT, password)

    def check_current_url(self):
        """Проверяет, что открыта страница регистрации"""
        self.page_have_url(REGISTRATION_URL)

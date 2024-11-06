import allure
from playwright.sync_api import Page

from utils.data import RandomData


@allure.title("Регистрация с незаполненными полями")
@allure.label("owner", "irauchuvatova")
def test_reg_all_empty_fields(page: Page, registration_page) -> None:
    with allure.step("Открыть страницу регистрации"):
        registration_page.goto()
    with allure.step("Нажать на кнопку Далее"):
        registration_page.click_submit_button()

    with allure.step("Проверить, что открыта страница регистрации"):
        registration_page.check_current_url()
    with allure.step("Проверить цвет и текст алерта под полем Имя пользователя"):
        registration_page.check_empty_user_name_alert()
    with allure.step("Проверить цвет и текст алерта под полем Электронная почта"):
        registration_page.check_empty_email_alert()
    with allure.step("Проверить цвет и текст алерта под полем Пароль"):
        registration_page.check_empty_password_alert()

@allure.title("Регистрация с паролем длиной 7 символов")
@allure.label("owner", "irauchuvatova")
def test_reg_short_password(page: Page, registration_page, randomdata: RandomData) -> None:
    username = randomdata.generate_random_name
    email = username + "@gmail.com"
    password = randomdata.generate_seven_symbol_pass

    with allure.step("Открыть страницу регистрации"):
        registration_page.goto()
    with allure.step("Заполнить поле Имя пользователя"):
        registration_page.input_username_field(username)
    with allure.step("Заполнить поле Электронная почта"):
        registration_page.input_email_field(email)
    with allure.step("Заполнить поле Пароль"):
        registration_page.input_password_field(password)
    with allure.step("Отметить чек-бос согласия с пользовательским соглашением"):
        registration_page.click_user_agreement_checkbox()
    with allure.step("Нажать на кнопку Далее"):
        registration_page.click_submit_button()

    with allure.step("Проверить, что открыта страница регистрации"):
        registration_page.check_current_url()
    with allure.step("Проверить цвет и текст алерта под полем Пароль"):
        registration_page.check_short_password_alert()

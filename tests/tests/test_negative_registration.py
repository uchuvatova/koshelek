from playwright.sync_api import Page

from utils.data import RandomData


def test_reg_all_empty_fields(page: Page, registration_page) -> None:
    registration_page.goto()
    registration_page.click_submit_button()

    registration_page.check_current_url()
    registration_page.check_empty_user_name_alert()
    registration_page.check_empty_email_alert()
    registration_page.check_empty_password_alert()


def test_reg_short_password(page: Page, registration_page, randomdata: RandomData) -> None:
    username = randomdata.generate_random_name
    email = username + "@gmail.com"
    password = randomdata.generate_seven_symbol_pass

    registration_page.goto()
    registration_page.input_username_field(username)
    registration_page.input_email_field(email)
    registration_page.input_password_field(password)
    registration_page.click_user_agreement_checkbox()
    registration_page.click_submit_button()

    registration_page.check_current_url()
    registration_page.check_short_password_alert()

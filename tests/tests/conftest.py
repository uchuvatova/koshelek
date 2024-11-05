import pytest
from playwright.sync_api import sync_playwright, Page

from tests.pages.registration_page import RegistrationPage
from utils.data import RandomData


@pytest.fixture
def page():
    """
    Запускает браузер Chrome
    Открывает окно браузера с указаными размерами
    После прохождения закрывается страница, браузер
    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(args=['--disable-notifications'], headless=False)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        yield page

        page.close()
        context.close()
        browser.close()


def handle_dialog(dialog):
    assert dialog.type == 'beforeunload'
    dialog.dismiss()


@pytest.fixture
def registration_page(page: Page):
    """Возвращает страницу регистрации"""
    return RegistrationPage(page)


@pytest.fixture
def randomdata():
    return RandomData()

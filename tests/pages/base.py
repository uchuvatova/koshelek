from playwright.sync_api import Page, Response, expect


class Base:
    """Базовые методы для переиспользования в классах страниц"""
    def __init__(self, page: Page):
        """
        Создает экземпляр класса Page, чтобы он был доступен во всех методах класса Base,
        что позволит выполнять действия на веб-страницах
        """
        self.page = page

    def open(self, uri) -> Response | None:
        """
        Открывает URL
        :param uri: str
        :return:
        """
        return self.page.goto(uri, wait_until='domcontentloaded')

    def click(self, locator: str) -> None:
        """
        Делает клик по локатору, при необходимости сам делает скролл к нужному элементу
        :param locator: str
        :return:
        """
        self.page.click(locator)

    def input(self, locator: str, text: str) -> None:
        """
        Вводит текст
        :param locator: str
        :param text: str
        :return:
        """
        self.page.type(locator, text)

    def element_has_text(self, locator: str, text: str) -> None:
        """
        Проверяет, что элемент содержит текст
        :param locator: str
        :param text: str
        :return:
        """
        expect(self.page.locator(locator)).to_have_text(text)

    def element_has_color(self, locator, color):
        """
        Проверяет, что элемент имеет цвет
        :param locator: str
        :param color: str
        :return:
        """
        expect(self.page.locator(locator)).to_have_css('caret-color', color)

    def page_have_url(self, url):
        """
        Проверяет, что страница имеет соответствующий url
        :param url: str
        :return:
        """
        expect(self.page).to_have_url(url)



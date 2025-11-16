from .base_page import BasePage


class MainPage(BasePage):
    """Page Object для главной страницы https://fitomarket.ru/"""

    PATH = "/"

    def open(self):
        """Открыть главную страницу."""
        super().open(self.PATH)

    def get_brand_in_title(self) -> str:
        """Возвращает заголовок страницы (для проверок бренда)."""
        return self.title


class BasePage:
    """Базовый класс для всех страниц сайта."""

    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url.rstrip("/")

    def open(self, path: str = "/"):
        """Открывает страницу по относительному пути."""
        url = self.base_url + path
        self.driver.get(url)

    @property
    def title(self) -> str:
        """Возвращает заголовок текущей страницы."""
        return self.driver.title


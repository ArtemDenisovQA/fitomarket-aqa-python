import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    """Фикстура для инициализации браузера Chrome."""
    options = Options()
    # Если хочешь видеть окно браузера — закомментируй строку ниже
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL тестируемого сайта."""
    return "https://fitomarket.ru/"


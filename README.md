# fitomarket-aqa-python

Pet-проект по автоматизации тестирования веб-сайта 
[fitomarket.ru](https://fitomarket.ru/) на Python.

Цель проекта — отработать написание UI-автотестов: работа с браузером, 
локаторами, тестовыми данными (Excel), отчётностью (Allure) и интеграцией 
с GitHub.

---

## Используемые технологии и инструменты

- **Язык:** Python 3.13  
- **Тестовый фреймворк:** `pytest`  
- **UI-автоматизация:** `Selenium WebDriver`  
- **Работа с Excel:** `openpyxl`  
- **Отчётность:** `Allure` + плагин `allure-pytest`  
- **Управление зависимостями:** `pip` + виртуальное окружение `venv`  
- **Система контроля версий:** Git  
- **Хостинг репозитория:** GitHub  
- **ОС разработчика:** macOS 13

---

## Структура проекта (план)

```text
fitomarket-aqa-python/
├── tests/              # тесты (pytest)
├── pages/              # Page Object-ы для страниц fitomarket.ru
├── data/               # тестовые данные, Excel и др.
├── config/             # конфигурация (URl, env, параметры запуска)
├── reports/            # отчёты тестовых прогонов (в т.ч. Allure)
├── venv/               # виртуальное окружение (не коммитится)
├── conftest.py         # общие фикстуры pytest
├── requirements.txt    # зависимости проекта
└── README.md

git clone https://github.com/ArtemDenisovQA/fitomarket-aqa-python.git
cd fitomarket-aqa-python

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

Базовые зависимости (план)

pytest

selenium

openpyxl

allure-pytest
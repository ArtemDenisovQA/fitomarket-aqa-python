from pages.main_page import MainPage


def test_main_page_title_contains_brand_name(browser, base_url):
    """
    Открываем главную страницу и проверяем, что в title есть слово 
'Фитомаркет'.

    Тест использует Page Object MainPage.
    """
    main_page = MainPage(browser, base_url)
    main_page.open()

    title = main_page.get_brand_in_title()
    assert "Фитомаркет" in title, (
        f"Ожидали увидеть 'Фитомаркет' в заголовке страницы, "
        f"но получили: {title!r}"
    )


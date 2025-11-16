def test_main_page_title_contains_brand_name(browser, base_url):
    """
    Открываем главную страницу и проверяем, что в title есть слово 
'Фитомаркет'.
    Базовая проверка, что сайт открывается и отдаёт ожидаемый заголовок.
    """
    browser.get(base_url)
    title = browser.title
    assert "Фитомаркет" in title, (
        f"Ожидали увидеть 'Фитомаркет' в заголовке страницы, "
        f"но получили: {title!r}"
    )


def test_hello_world(browser):
    browser.get(f"{browser.base_url}")
    assert browser.title == "Your Store"

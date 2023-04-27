import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://192.168.8.169/")
    parser.addoption("--headless", action="store_true")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    driver = None

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.headless = True
        driver = webdriver.Firefox(options=options)
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)
    elif browser_name == "safari":
        driver = webdriver.Safari()

    driver.base_url = base_url

    driver.maximize_window()

    yield driver

    driver.quit()

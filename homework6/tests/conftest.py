import os
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.edge.service import Service as EdgeService


DRIVERS = os.path.expanduser("~/PycharmProjects/drivers")


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox", "opera", "safari", "edge", "yandex"],
        help="browser for testing"
    )
    parser.addoption(
        "--url",
        default="https://demo.opencart.com/",
        help="url for testing"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="flag for testing without visible browser")


@pytest.fixture
def driver(request):
    _driver = None
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        service = ChromiumService(executable_path=f"{DRIVERS}/chromedriver")
        options.headless = headless
        _driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        service = FFService(executable_path=f"{DRIVERS}/geckodriver")
        options.headless = headless
        _driver = webdriver.Firefox(service=service, options=options)
    elif browser == "opera":
        _driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")
    elif browser == "safari":
        service = SafariService(executable_path=f"{DRIVERS}/safaridriver")
        _driver = webdriver.Safari(service=service)
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        service = EdgeService(executable_path=f"{DRIVERS}/msedgedriver")
        options.headless = headless
        _driver = webdriver.Edge(service=service, options=options)
    elif browser == "yandex":
        options = webdriver.ChromeOptions()
        service = ChromiumService(executable_path=f"{DRIVERS}/yandexdriver")
        options.headless = headless
        _driver = webdriver.Chrome(service=service, options=options)

    _driver.maximize_window()

    _driver.base_url = base_url
    yield _driver

    _driver.quit()

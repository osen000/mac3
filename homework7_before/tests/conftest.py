import os
import pytest
import logging
import datetime

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

    parser.addoption(
        "--bversion",
        action="store",
        default="99.0",
        help="browser version")

    parser.addoption(
        "--executor",
        default="192.168.75.1",
        help="who started test, example selenoid")

    parser.addoption(
        "--log_level",
        action="store",
        default="DEBUG")


@pytest.fixture
def driver(request):
    _driver = None
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger('_driver')
    logger.handlers.clear()
    test_name = request.node.name

    logger.addHandler(logging.FileHandler(f"logs/{test_name}.log"))
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(test_name, datetime.datetime.now()))

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

    _driver.test_name = test_name
    _driver.log_level = log_level
    _driver.maximize_window()
    _driver.base_url = base_url

    logger.info("Browser:{}".format(browser, _driver.capabilities))


    # yield _driver - альтернативное окончание
    def fin():
        _driver.quit()
        logger.info("===> Test {} finished at {}".format(test_name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return _driver


@pytest.fixture(scope="session", autouse=True)
def get_environment(pytestconfig, request):
    props = {
        'Browser': request.config.getoption("--browser"),
        'Browser.Version': request.config.getoption("--bversion"),
        'Executor': request.config.getoption("--executor")
    }

    tests_root = pytestconfig.rootdir
    with open(f'{tests_root}/allure-results/environment.properties', 'w') as f:
        env_props = '\n'.join([f'{k}={v}' for k, v in props.items()])
        f.write(env_props)

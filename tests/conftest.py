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
def remote(request):
    _driver = None
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    base_url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger('_driver')
    logger.handlers.clear()
    test_name = request.node.name

    logger.addHandler(logging.FileHandler(f"logs/{test_name}.log"))
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(test_name, datetime.datetime.now()))
    _driver = webdriver.Remote(
        command_executor=f"http://{executor}:4444/wd/hub",
        desired_capabilities={"browserName": browser}
    )
    _driver.implicitly_wait(2)

    _driver.test_name = test_name
    _driver.log_level = log_level
    _driver.maximize_window()
    _driver.base_url = base_url

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

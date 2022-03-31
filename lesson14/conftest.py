import pytest
import logging

from config import CHROMEDRIVER
from selenium import webdriver

logging.basicConfig(level=logging.ERROR)


@pytest.fixture
def browser(request):
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER)
    request.addfinalizer(driver.close)
    return driver

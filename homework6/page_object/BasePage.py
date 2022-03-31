from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver, tolerance):
        self.driver = driver
        self.tolerance = tolerance

    def verify_element_presence(self, params):
        for locator in params:
            try:
                WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(locator))
            except TimeoutException:
                raise AssertionError("Locator not found: {}".format(locator))

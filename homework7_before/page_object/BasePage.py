from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import allure
import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_object.elements.AdminLogin import AdminLogin
from page_object.elements.CatalogAdmin import CatalogAdmin


class BasePage:
    def __init__(self, driver, tolerance=5):
        self.driver = driver
        self.tolerance = tolerance
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.handlers.clear()
        self.f_handler = logging.FileHandler(f"logs/{driver.test_name}.log")
        self.f_handler.setLevel(level=self.driver.log_level)
        self.f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.f_handler.setFormatter(self.f_format)
        self.logger.addHandler(self.f_handler)
        self.params = AdminLogin.locators_for_login
        self.params_catalog = CatalogAdmin.locators_before_click


    @allure.step("Verify element by locator")
    def verify_element_presence(self, params):
        for locator in params:
            self.logger.info("Find locator: {}".format(locator))
            try:
                WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(locator))
            except TimeoutException:
                raise AssertionError("Locator not found: {}".format(locator))

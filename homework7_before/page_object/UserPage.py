from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_object.elements.Registration import Registration
import allure
import logging
import helpers
from page_object.BasePage import BasePage


class UserPage(BasePage):
    # def __init__(self, driver, tolerance):
    #     self.driver = driver
    #     self.tolerance = tolerance
    #     self.logger = logging.getLogger(type(self).__name__)
    #     self.logger.handlers.clear()
    #     self.f_handler = logging.FileHandler(f"logs/{driver.test_name}.log")
    #     self.f_handler.setLevel(level=self.driver.log_level)
    #     self.f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #     self.f_handler.setFormatter(self.f_format)
    #     self.logger.addHandler(self.f_handler)


    @allure.step("Data for create user")
    def input_new_user_data(self, locator, value):
        self.logger.info("Input {} in input {}".format(value, locator))
        self.driver.find_element(*locator).click()
        self.driver.find_element(*locator).send_keys(value)

    @allure.step("Random email for create user")
    def input_new_user_email(self, locator):
        self.logger.info("Input {}".format(locator))
        self.driver.find_element(*locator).click()
        self.value = helpers.random_email()
        self.driver.find_element(*locator).send_keys(self.value)

    @allure.step("Find element for click")
    def find_element_for_user_data(self, locator):
        self.logger.info("Clicking element: {}".format(locator))
        self.driver.find_element(*locator).click()

    @allure.step("Text verify")
    def text_confirm(self):
        self.logger.info("Find locator: {}".format(Registration.NEW_USER_CONFIRM))
        try:
            WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(Registration.NEW_USER_CONFIRM))
        except TimeoutException:
            raise AssertionError("Locator not found: {}".format(Registration.NEW_USER_CONFIRM))

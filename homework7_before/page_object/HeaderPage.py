from page_object.elements.Main import Main
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import allure
import logging
from page_object.BasePage import BasePage


class HeaderPage(BasePage):
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

    @allure.step("Navigate by header menu")
    def header_menu_click(self):
        self.logger.info("Clicking element: {}".format(Main.HEADER_LK))
        self.driver.find_element(*Main.HEADER_LK).click()
        self.driver.find_element(*Main.MENU_REGISTER).click()

    @allure.step("Enter to \"currency\" menu")
    def header_menu_click_currency(self):
        self.logger.info("Clicking element: {}".format(Main.HEADER_BUTTON_CURRENCY))
        self.driver.find_element(*Main.HEADER_BUTTON_CURRENCY).click()
        self.driver.find_element(*Main.SELECT_EUR).click()

    @allure.step("Text verify")
    def text_confirm(self):
        self.logger.info("Find locator: {}".format(Main.CONFIRM_SELECT_EUR))
        try:
            WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(Main.CONFIRM_SELECT_EUR))
        except TimeoutException:
            raise AssertionError("Locator not found: {}".format(Main.CONFIRM_SELECT_EUR))

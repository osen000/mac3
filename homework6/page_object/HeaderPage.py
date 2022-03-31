from page_object.elements.Main import Main
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


class HeaderPage:

    def __init__(self, driver, tolerance):
        self.driver = driver
        self.tolerance = tolerance

    def header_menu_click(self):
        self.driver.find_element(*Main.HEADER_LK).click()
        self.driver.find_element(*Main.MENU_REGISTER).click()

    def header_menu_click_currency(self):
        self.driver.find_element(*Main.HEADER_BUTTON_CURRENCY).click()
        self.driver.find_element(*Main.SELECT_EUR).click()

    def text_confirm(self):
        try:
            WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(Main.CONFIRM_SELECT_EUR))
        except TimeoutException:
            raise AssertionError("Locator not found: {}".format(Main.CONFIRM_SELECT_EUR))

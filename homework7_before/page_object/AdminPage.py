from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_object.elements.AdminLogin import AdminLogin
from page_object.elements.CatalogAdmin import CatalogAdmin
from page_object.BasePage import BasePage
import allure
import logging


class AdminPage(BasePage):
    # def __init__(self, driver, tolerance=5):
    #     self.driver = driver
    #     self.tolerance = tolerance
    #     self.params = AdminLogin.locators_for_login
    #     self.params_catalog = CatalogAdmin.locators_before_click
    #     self.logger = logging.getLogger(type(self).__name__)
    #     self.logger.handlers.clear()
    #     self.f_handler = logging.FileHandler(f"logs/{self.driver.test_name}.log")
    #     self.f_handler.setLevel(level=self.driver.log_level)
    #     self.f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #     self.f_handler.setFormatter(self.f_format)
    #     self.logger.addHandler(self.f_handler)

    @allure.step("Verify element by locator")
    def verify_element_presence(self):
        for locator in self.params:
            self.logger.info("Find locator: {}".format(locator))
            try:
                WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(locator))
            except TimeoutException:
                raise AssertionError("Locator not found: {}".format(locator))

    @allure.step("Login")
    def login_with(self, username, password):
        self.logger.info("Login with username: {}, password: {}".format(username, password))
        self.driver.find_element(*AdminLogin.INPUT_USERNNAME).clear()
        self.driver.find_element(*AdminLogin.INPUT_USERNNAME).send_keys(username)
        self.driver.find_element(*AdminLogin.INPUT_PASSWORD).clear()
        self.driver.find_element(*AdminLogin.INPUT_PASSWORD).send_keys(password)
        self.driver.find_element(*AdminLogin.SUBMIT_ENTER).click()

    @allure.step("Wait element")
    def text_present_form(self):
        self.logger.info("Wait element: {}".format(AdminLogin.PATH_TEXT_FOR_LOGIN))
        try:
            WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located
                                                             (AdminLogin.PATH_TEXT_FOR_LOGIN))
        except TimeoutException:
            raise AssertionError("Text not found: {}".format(AdminLogin.PATH_TEXT_FOR_LOGIN))

    @allure.step("Enter to menu")
    def enter_to_menu(self):
        self.logger.info("Click element: {}".format(CatalogAdmin.MENU_CATALOG_PRODUCTS))
        WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located
                                                         (CatalogAdmin.MENU_CATALOG))
        self.driver.find_element(*CatalogAdmin.MENU_CATALOG).click()
        WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located
                                                         (CatalogAdmin.MENU_CATALOG_PRODUCTS))
        self.driver.find_element(*CatalogAdmin.MENU_CATALOG_PRODUCTS).click()

    @allure.step("Verify element in catalog")
    def verify_element_presence_catalog(self):
        for locator in self.params_catalog:
            self.logger.info("Find locator: {}".format(locator))
            try:
                WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(locator))
            except TimeoutException:
                raise AssertionError("Locator not found: {}".format(locator))

    @allure.step("Verify title in catalog")
    def title_present_form(self):
        self.logger.info("Verify title: {}".format(CatalogAdmin.TITLE_WORK))
        try:
            WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(CatalogAdmin.TITLE_WORK))
        except TimeoutException:
            raise AssertionError("Text not found: {}".format(CatalogAdmin.TITLE_WORK))

    @allure.step("Add new item - verify title")
    def add_item_title(self):
        self.logger.info("Verify title: {}".format(CatalogAdmin.TITLE_NEW_ITEM))
        self.driver.find_element(*CatalogAdmin.BUTTON_ADD_ITEM).click()
        WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(CatalogAdmin.TITLE_NEW_ITEM))

    @allure.step("Data fot item form")
    def item_form(self, locator, value):
        self.logger.info("Input {} in input {}".format(value, locator))
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @allure.step("Add new item - click button save")
    def add_item_save(self):
        self.logger.info("Verify title: {}".format(CatalogAdmin.SUBMIT_SAVE))
        self.driver.find_element(*CatalogAdmin.SUBMIT_SAVE).click()

    @allure.step("Find item")
    def find_new_item(self, value):
        self.logger.info("Find value {} in element {}".format(value, CatalogAdmin.FILTR_BUTTON))
        WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(CatalogAdmin.TITLE_WORK))
        self.driver.find_element(*CatalogAdmin.FILTR_NAME).clear()
        self.driver.find_element(*CatalogAdmin.FILTR_NAME).send_keys(value)
        self.driver.find_element(*CatalogAdmin.FILTR_BUTTON).click()
        WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(CatalogAdmin.TITLE_WORK))

    @allure.step("Delete item")
    def delete_new_item(self, value):
        self.logger.info("Delete value {} ".format(value))
        self.driver.find_element(*CatalogAdmin.ITEM_CHECKBOX).click()
        self.driver.find_element(*CatalogAdmin.DELETE_BUTTON).click()
        confirm_alert = self.driver.switch_to.alert
        confirm_alert.accept()

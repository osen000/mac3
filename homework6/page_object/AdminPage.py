from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_object.elements.AdminLogin import AdminLogin
from page_object.elements.CatalogAdmin import CatalogAdmin


class AdminPage:

    def __init__(self, driver, tolerance):
        self.driver = driver
        self.tolerance = tolerance
        self.params = AdminLogin.locators_for_login
        self.params_catalog = CatalogAdmin.locators_before_click

    def verify_element_presence(self):
        for locator in self.params:
            try:
                WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(locator))
            except TimeoutException:
                raise AssertionError("Locator not found: {}".format(locator))

    def login_with(self, username, password):
        self.driver.find_element(*AdminLogin.INPUT_USERNNAME).clear()
        self.driver.find_element(*AdminLogin.INPUT_USERNNAME).send_keys(username)
        self.driver.find_element(*AdminLogin.INPUT_PASSWORD).clear()
        self.driver.find_element(*AdminLogin.INPUT_PASSWORD).send_keys(password)
        self.driver.find_element(*AdminLogin.SUBMIT_ENTER).click()

    def text_present_form(self):
        try:
            WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located
                                                             (AdminLogin.PATH_TEXT_FOR_LOGIN))
        except TimeoutException:
            raise AssertionError("Text not found: {}".format(AdminLogin.PATH_TEXT_FOR_LOGIN))

    def enter_to_menu(self):
        WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located
                                                         (CatalogAdmin.MENU_CATALOG))
        self.driver.find_element(*CatalogAdmin.MENU_CATALOG).click()
        WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located
                                                         (CatalogAdmin.MENU_CATALOG_PRODUCTS))
        self.driver.find_element(*CatalogAdmin.MENU_CATALOG_PRODUCTS).click()

    def verify_element_presence_catalog(self):
        for locator in self.params_catalog:
            try:
                WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(locator))
            except TimeoutException:
                raise AssertionError("Locator not found: {}".format(locator))

    def title_present_form(self):
        try:
            WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(CatalogAdmin.TITLE_WORK))
        except TimeoutException:
            raise AssertionError("Text not found: {}".format(CatalogAdmin.TITLE_WORK))

    def add_item(self):
        self.driver.find_element(*CatalogAdmin.BUTTON_ADD_ITEM).click()
        WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(CatalogAdmin.TITLE_NEW_ITEM))
        self.driver.find_element(*CatalogAdmin.PRODUCT_NAME).clear()
        self.driver.find_element(*CatalogAdmin.PRODUCT_NAME).send_keys("123")
        self.driver.find_element(*CatalogAdmin.DESCRIPTION).send_keys("123")
        self.driver.find_element(*CatalogAdmin.PRODUCT_META_TAG_TITLE).clear()
        self.driver.find_element(*CatalogAdmin.PRODUCT_META_TAG_TITLE).send_keys("123")
        self.driver.find_element(*CatalogAdmin.PRODUCT_META_TAG_DESCRIPTION).clear()
        self.driver.find_element(*CatalogAdmin.PRODUCT_META_TAG_DESCRIPTION).send_keys("123")
        self.driver.find_element(*CatalogAdmin.PRODUCT_META_TAG_KEYWORDS).clear()
        self.driver.find_element(*CatalogAdmin.PRODUCT_META_TAG_KEYWORDS).send_keys("123")
        self.driver.find_element(*CatalogAdmin.PRODUCT_TAG).clear()
        self.driver.find_element(*CatalogAdmin.PRODUCT_TAG).send_keys("123")
        self.driver.find_element(*CatalogAdmin.SUBMIT_SAVE).click()

    def find_new_item(self):
        WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(CatalogAdmin.TITLE_WORK))
        self.driver.find_element(*CatalogAdmin.FILTR_NAME).clear()
        self.driver.find_element(*CatalogAdmin.FILTR_NAME).send_keys("123")
        self.driver.find_element(*CatalogAdmin.FILTR_BUTTON).click()
        WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(CatalogAdmin.TITLE_WORK))

    def delete_new_item(self):
        self.driver.find_element(*CatalogAdmin.ITEM_CHECKBOX).click()
        self.driver.find_element(*CatalogAdmin.DELETE_BUTTON).click()
        confirm_alert = self.driver.switch_to.alert
        confirm_alert.accept()

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from page_object.elements.Registration import Registration


class UserPage:

    def __init__(self, driver, tolerance):
        self.driver = driver
        self.tolerance = tolerance

    def input_new_user_data(self):
        self.driver.find_element(*Registration.INPUT_FIRST_NAME).click()
        self.driver.find_element(*Registration.INPUT_FIRST_NAME).send_keys("Иван")
        self.driver.find_element(*Registration.INPUT_LAST_NAME).click()
        self.driver.find_element(*Registration.INPUT_LAST_NAME).send_keys("Иванов")
        self.driver.find_element(*Registration.INPUT_EMAIL).click()
        self.driver.find_element(*Registration.INPUT_EMAIL).send_keys("dfg@ert.ert")
        self.driver.find_element(*Registration.INPUT_PHONE).click()
        self.driver.find_element(*Registration.INPUT_PHONE).send_keys("1234567890")

        self.driver.find_element(*Registration.INPUT_PASSWORD).click()
        self.driver.find_element(*Registration.INPUT_PASSWORD).send_keys("1234567890")
        self.driver.find_element(*Registration.INPUT_PASSWORD_CONFIRM).click()
        self.driver.find_element(*Registration.INPUT_PASSWORD_CONFIRM).send_keys("1234567890")

        self.driver.find_element(*Registration.CHECKBOX_PRIVACY_POLICY).click()
        self.driver.find_element(*Registration.SUBMIT_CONTINUE).click()

    def text_confirm(self):
        try:
            WebDriverWait(self.driver, self.tolerance).until(ec.visibility_of_element_located(Registration.NEW_USER_CONFIRM))
        except TimeoutException:
            raise AssertionError("Locator not found: {}".format(Registration.NEW_USER_CONFIRM))

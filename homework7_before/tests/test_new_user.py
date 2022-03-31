from page_object.BasePage import BasePage
from page_object.HeaderPage import HeaderPage
from page_object.UserPage import UserPage
from page_object.elements.Registration import Registration
import allure
import helpers


@allure.severity(allure.severity_level.NORMAL)
def test_new_user(driver):
    """Добавить нового пользователя"""
    driver.get(driver.base_url)
    HeaderPage(driver, 5).header_menu_click()
    BasePage(driver, 5).verify_element_presence(Registration.locators)
    UserPage(driver, 5).input_new_user_data(Registration.INPUT_FIRST_NAME, "Иван")
    UserPage(driver, 5).input_new_user_data(Registration.INPUT_LAST_NAME, "Иванов")
    UserPage(driver, 5).input_new_user_email(Registration.INPUT_EMAIL)
    UserPage(driver, 5).input_new_user_data(Registration.INPUT_PHONE, "1234567890")
    UserPage(driver, 5).input_new_user_data(Registration.INPUT_PASSWORD, "1234567890")
    UserPage(driver, 5).input_new_user_data(Registration.INPUT_PASSWORD_CONFIRM, "1234567890")
    UserPage(driver, 5).find_element_for_user_data(Registration.CHECKBOX_PRIVACY_POLICY)
    UserPage(driver, 5).find_element_for_user_data(Registration.SUBMIT_CONTINUE)
    UserPage(driver, 5).text_confirm()


@allure.severity(allure.severity_level.MINOR)
def test_change_currency(driver):
    """Поменять валюту"""
    driver.get(driver.base_url)
    HeaderPage(driver, 5).header_menu_click_currency()
    HeaderPage(driver, 5).text_confirm()

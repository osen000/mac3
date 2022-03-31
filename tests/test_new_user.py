from page_object.BasePage import BasePage
from page_object.HeaderPage import HeaderPage
from page_object.UserPage import UserPage
from page_object.elements.Registration import Registration
import allure


@allure.severity(allure.severity_level.NORMAL)
def test_new_user(remote):
    """Добавить нового пользователя"""
    remote.get(remote.base_url)
    HeaderPage(remote, 5).header_menu_click()
    BasePage(remote, 5).verify_element_presence(Registration.locators)
    UserPage(remote, 5).input_new_user_data(Registration.INPUT_FIRST_NAME, "Иван")
    UserPage(remote, 5).input_new_user_data(Registration.INPUT_LAST_NAME, "Иванов")
    UserPage(remote, 5).input_new_user_email(Registration.INPUT_EMAIL)
    UserPage(remote, 5).input_new_user_data(Registration.INPUT_PHONE, "1234567890")
    UserPage(remote, 5).input_new_user_data(Registration.INPUT_PASSWORD, "1234567890")
    UserPage(remote, 5).input_new_user_data(Registration.INPUT_PASSWORD_CONFIRM, "1234567890")
    UserPage(remote, 5).find_element_for_user_data(Registration.CHECKBOX_PRIVACY_POLICY)
    UserPage(remote, 5).find_element_for_user_data(Registration.SUBMIT_CONTINUE)
    UserPage(remote, 5).text_confirm()


@allure.severity(allure.severity_level.MINOR)
def test_change_currency(remote):
    """Поменять валюту"""
    remote.get(remote.base_url)
    HeaderPage(remote, 5).header_menu_click_currency()
    HeaderPage(remote, 5).text_confirm()

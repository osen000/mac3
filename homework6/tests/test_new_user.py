from page_object.BasePage import BasePage
from page_object.HeaderPage import HeaderPage
from page_object.UserPage import UserPage
from page_object.elements.Registration import Registration
import os


def test_new_user(driver):
    """Добавить нового пользователя"""
    driver.get(driver.base_url)
    HeaderPage(driver, 5).header_menu_click()
    BasePage(driver, 5).verify_element_presence(Registration.locators)
    UserPage(driver, 5).input_new_user_data()
    UserPage(driver, 5).text_confirm()


def test_change_currency(driver):
    """Поменять валюту"""
    driver.get(driver.base_url)
    HeaderPage(driver, 5).header_menu_click_currency()
    HeaderPage(driver, 5).text_confirm()

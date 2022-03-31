from page_object.BasePage import BasePage
from page_object.elements.AdminLogin import AdminLogin
from page_object.elements.Catalog import Catalog
from page_object.elements.ItemPost import ItemPost
from page_object.elements.Main import Main
from page_object.elements.Registration import Registration


def test_admin_login(driver):
    """Поиск элементов на странице авторизации админа"""
    driver.get(driver.base_url + f"admin")
    BasePage(driver, 5).verify_element_presence(AdminLogin.locators)


def test_catalog(driver):
    """Поиск элементов в каталоге"""
    driver.get(driver.base_url + f"index.php?route=product/category&path=20")
    BasePage(driver, 5).verify_element_presence(Catalog.locators)


def test_item_post(driver):
    """Поиск элементов в карточке товара"""
    driver.get(driver.base_url + f"index.php?route=product/product&path=20&product_id=42&sort=p.sort_order&order=ASC")
    BasePage(driver, 5).verify_element_presence(ItemPost.locators)


def test_main_page(driver):
    """Поиск элементов на главной странице"""
    driver.get(driver.base_url)
    BasePage(driver, 5).verify_element_presence(Main.locators)


def test_user_registration(driver):
    """Поиск элементов на странице регистрации пользователя"""
    driver.get(driver.base_url + f"index.php?route=account/register")
    BasePage(driver, 5).verify_element_presence(Registration.locators)

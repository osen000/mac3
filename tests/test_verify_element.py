from page_object.BasePage import BasePage
from page_object.elements.AdminLogin import AdminLogin
from page_object.elements.Catalog import Catalog
from page_object.elements.ItemPost import ItemPost
from page_object.elements.Main import Main
from page_object.elements.Registration import Registration
import allure


@allure.severity(allure.severity_level.CRITICAL)
def test_admin_login_verify(remote):
    """Поиск элементов на странице авторизации админа"""
    remote.get(remote.base_url + f"admin")
    BasePage(remote, 5).verify_element_presence(AdminLogin.locators)


@allure.severity(allure.severity_level.CRITICAL)
def test_catalog_verify(remote):
    """Поиск элементов в каталоге"""
    remote.get(remote.base_url + f"index.php?route=product/category&path=20")
    BasePage(remote, 5).verify_element_presence(Catalog.locators)


@allure.severity(allure.severity_level.CRITICAL)
def test_item_post_verify(remote):
    """Поиск элементов в карточке товара"""
    remote.get(remote.base_url + f"index.php?route=product/product&path=20&product_id=42&sort=p.sort_order&order=ASC")
    BasePage(remote, 5).verify_element_presence(ItemPost.locators)


@allure.severity(allure.severity_level.CRITICAL)
def test_main_page_verify(remote):
    """Поиск элементов на главной странице"""
    remote.get(remote.base_url)
    BasePage(remote, 5).verify_element_presence(Main.locators)


@allure.severity(allure.severity_level.CRITICAL)
def test_user_registration_verify(remote):
    """Поиск элементов на странице регистрации пользователя"""
    remote.get(remote.base_url + f"index.php?route=account/register")
    BasePage(remote, 5).verify_element_presence(Registration.locators)

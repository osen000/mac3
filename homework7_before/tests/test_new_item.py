from page_object.AdminPage import AdminPage
from page_object.elements.CatalogAdmin import CatalogAdmin
import allure


@allure.title("Залогинаться в приложении администратора")
@allure.severity(allure.severity_level.CRITICAL)
def test_admin_login(driver):
    # """Залогинаться в приложении администратора"""
    driver.get(driver.base_url + f"admin")
    AdminPage(driver).verify_element_presence()
    AdminPage(driver).login_with("demo", "demo")
    AdminPage(driver).text_present_form()


@allure.title("Добавление товара в админке")
@allure.severity(allure.severity_level.NORMAL)
def test_new_item(driver):
    """Добавление товара в админке"""
    driver.get(driver.base_url + f"admin")
    AdminPage(driver).login_with("demo", "demo")
    AdminPage(driver).verify_element_presence_catalog() #проверили наличие элементов
    AdminPage(driver).enter_to_menu() #клик по каталогу
    AdminPage(driver).title_present_form() #проверяем наличие заголовка
    AdminPage(driver).add_item_title()
    # данные для заполнения формы
    AdminPage(driver).item_form(CatalogAdmin.PRODUCT_NAME, "123")
    AdminPage(driver).item_form(CatalogAdmin.DESCRIPTION, "123")
    AdminPage(driver).item_form(CatalogAdmin.PRODUCT_META_TAG_TITLE, "123")
    AdminPage(driver).item_form(CatalogAdmin.PRODUCT_META_TAG_DESCRIPTION, "123")
    AdminPage(driver).item_form(CatalogAdmin.PRODUCT_META_TAG_KEYWORDS, "123")
    AdminPage(driver).item_form(CatalogAdmin.PRODUCT_TAG, "123")
    AdminPage(driver).add_item_save()


@allure.title("Удаление товара в админке")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_item(driver):
    """Удаление товара в админке"""
    driver.get(driver.base_url + f"admin")
    AdminPage(driver).login_with("demo", "demo")
    AdminPage(driver).verify_element_presence_catalog()  # проверили наличие элементов
    AdminPage(driver).enter_to_menu()  # клик по каталогу
    AdminPage(driver).title_present_form()  # проверяем наличие заголовка
    AdminPage(driver).find_new_item("123")  # фильтр для поиска нового товара
    AdminPage(driver).delete_new_item("123")  # удаляем ранее созданный товар

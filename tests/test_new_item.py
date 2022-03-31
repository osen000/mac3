from page_object.AdminPage import AdminPage
from page_object.elements.CatalogAdmin import CatalogAdmin
import allure


@allure.title("Залогинаться в приложении администратора")
@allure.severity(allure.severity_level.CRITICAL)
def test_admin_login(remote):
    # """Залогинаться в приложении администратора"""
    remote.get(remote.base_url + f"admin")
    AdminPage(remote).verify_element_presence()
    AdminPage(remote).login_with("demo", "demo")
    AdminPage(remote).text_present_form()


@allure.title("Добавление товара в админке")
@allure.severity(allure.severity_level.NORMAL)
def test_new_item(remote):
    """Добавление товара в админке"""
    remote.get(remote.base_url + f"admin")
    AdminPage(remote).login_with("demo", "demo")
    AdminPage(remote).verify_element_presence_catalog() #проверили наличие элементов
    AdminPage(remote).enter_to_menu() #клик по каталогу
    AdminPage(remote).title_present_form() #проверяем наличие заголовка
    AdminPage(remote).add_item_title()
    # данные для заполнения формы
    AdminPage(remote).item_form(CatalogAdmin.PRODUCT_NAME, "123")
    AdminPage(remote).item_form(CatalogAdmin.DESCRIPTION, "123")
    AdminPage(remote).item_form(CatalogAdmin.PRODUCT_META_TAG_TITLE, "123")
    AdminPage(remote).item_form(CatalogAdmin.PRODUCT_META_TAG_DESCRIPTION, "123")
    AdminPage(remote).item_form(CatalogAdmin.PRODUCT_META_TAG_KEYWORDS, "123")
    AdminPage(remote).item_form(CatalogAdmin.PRODUCT_TAG, "123")
    AdminPage(remote).add_item_save()


@allure.title("Удаление товара в админке")
@allure.severity(allure.severity_level.NORMAL)
def test_delete_item(remote):
    """Удаление товара в админке"""
    remote.get(remote.base_url + f"admin")
    AdminPage(remote).login_with("demo", "demo")
    AdminPage(remote).verify_element_presence_catalog()  # проверили наличие элементов
    AdminPage(remote).enter_to_menu()  # клик по каталогу
    AdminPage(remote).title_present_form()  # проверяем наличие заголовка
    AdminPage(remote).find_new_item("123")  # фильтр для поиска нового товара
    AdminPage(remote).delete_new_item("123")  # удаляем ранее созданный товар

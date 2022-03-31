from page_object.AdminPage import AdminPage
import time


def test_admin_login(driver):
    """Залогинаться в приложении администратора"""
    driver.get(driver.base_url + f"admin")
    AdminPage(driver, 5).verify_element_presence()
    AdminPage(driver, 5).login_with("demo", "demo")
    AdminPage(driver, 5).text_present_form()


def test_new_item(driver):
    """Добавление товара в админке"""
    driver.get(driver.base_url + f"admin")
    AdminPage(driver, 5).login_with("demo", "demo")
    AdminPage(driver, 5).verify_element_presence_catalog() #проверили наличие элементов
    AdminPage(driver, 5).enter_to_menu() #клик по каталогу
    AdminPage(driver, 5).title_present_form() #проверяем наличие заголовка
    AdminPage(driver, 5).add_item() #добавляем товар
    time.sleep(2)


def test_delete_item(driver):
    """Удаление товара в админке"""
    driver.get(driver.base_url + f"admin")
    AdminPage(driver, 5).login_with("demo", "demo")
    AdminPage(driver, 5).verify_element_presence_catalog()  # проверили наличие элементов
    AdminPage(driver, 5).enter_to_menu()  # клик по каталогу
    AdminPage(driver, 5).title_present_form()  # проверяем наличие заголовка
    AdminPage(driver, 5).find_new_item()  # фильтр для поиска нового товара
    AdminPage(driver, 5).delete_new_item()  # удаляем ранее созданный товар
    time.sleep(10)

from selenium.webdriver.common.by import By


class CatalogAdmin:
    TITLE_PAGE = (By.XPATH, "//img[@title='OpenCart']")
    MENU_CATALOG = (By.XPATH, "//*[@id='menu-catalog']//*[text()=' Catalog']")
    MENU_CATALOG_PRODUCTS = (By.CSS_SELECTOR, "a[href*='product']")
    TITLE_WORK = (By.XPATH, "//*[@id='content']//h1[text()='Products']")
    BUTTON_ADD_ITEM = (By.XPATH, "//*[@data-original-title='Add New']")
    TITLE_NEW_ITEM = (By.XPATH, "//*[@id='content']//*[text()=' Add Product']")
    PRODUCT_NAME = (By.XPATH, "//*[@id='input-name1']")
    DESCRIPTION = (By.XPATH, "//*[@class='note-editable panel-body']/p")
    PRODUCT_META_TAG_TITLE = (By.XPATH, "//*[@id='input-meta-title1']")
    PRODUCT_META_TAG_DESCRIPTION = (By.XPATH, "//*[@id='input-meta-description1']")
    PRODUCT_META_TAG_KEYWORDS = (By.XPATH, "//*[@id='input-meta-keyword1']")
    PRODUCT_TAG = (By.XPATH, "//*[@id='input-tag1']")
    SUBMIT_SAVE = (By.XPATH, "//*[@data-original-title='Save']")
    FILTR_NAME = (By.XPATH, "//*[@name='filter_name']")
    FILTR_BUTTON = (By.XPATH, "//*[@id='button-filter']")
    FILTR_ITEM = (By.XPATH, "//*[@id='form-product']//td[text()='123']")
    ITEM_CHECKBOX = (By.XPATH, "//*[@id='form-product']//input")
    DELETE_BUTTON = (By.XPATH, "//*[@data-original-title='Delete']")
    CONFIRM_YES = (By.XPATH, "//*[@data-original-title='Delete']")

    locators_before_click = [
        TITLE_PAGE,
        MENU_CATALOG
    ]

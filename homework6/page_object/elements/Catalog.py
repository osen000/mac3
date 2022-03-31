from selenium.webdriver.common.by import By


class Catalog:
    TITLE_PAGE = (By.LINK_TEXT, "Desktops")
    PRODUCT_CATEGORY_PATH = (By.CSS_SELECTOR, "[class='fa fa-home']")
    PRODUCT_CATEGORY_NAME = (By.XPATH, "//*[@id='product-category']//a[text()='Desktops']")
    CONTENT_LABEL = (By.XPATH, "//*[@id='content']//h2[text()='Desktops']")
    PICTURE = (By.CSS_SELECTOR, "img[src$='.jpg'][title='Desktops']")
    SEARCH_CONTENT = (By.XPATH, "//*[@id='content']/h3[text()='Refine Search']")
    MENU_PC = (By.XPATH, "//*[@id='content']//a[text()='PC (0)']")
    MENU_MAC = (By.XPATH, "//*[@id='content']//a[text()='Mac (1)']")
    CLASS_LABEL = (By.CSS_SELECTOR, "[class='fa fa-th-list']")
    CLASS_LABEL_TH = (By.CSS_SELECTOR, "[class='fa fa-th']")
    COMPARE = (By.CSS_SELECTOR, "[id='compare-total']")
    LABEL_LIST_SELECT = (By.CSS_SELECTOR, "label[for='input-sort']")
    INPUT_SELECT = (By.CSS_SELECTOR, "select[id='input-sort']")
    INPUT_SELECT_DEFAULT = (By.XPATH, "//*[@id='input-sort']/option[text()='Default']")
    LABEL_SHOW = (By.XPATH, "//*[@id='content']//label[text()='Show:']")
    LIMIT_ROW = (By.XPATH, "//*[@id='input-limit']/option[text()='15']")
    PRODUCT_GRID = (By.XPATH, "//*[@class='product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12']")
    COUNT_PAGE = (By.XPATH, "//*[@id='content']//div[text()='Showing 1 to 12 of 12 (1 Pages)']")
    LIST_GROUP = (By.CLASS_NAME, "list-group")
    COUNT_DESCTOP = (By.XPATH, "//a[text()='Desktops (13)']")
    LIST_GROUP_ITEM = (By.XPATH, "//*[@class='list-group-item']")
    BANNER = (By.CSS_SELECTOR, "img[src$='.jpg'][alt='HP Banner']")

    locators = [
        TITLE_PAGE,
        PRODUCT_CATEGORY_PATH,
        PRODUCT_CATEGORY_NAME,
        CONTENT_LABEL,
        PICTURE,
        SEARCH_CONTENT,
        MENU_PC,
        MENU_MAC,
        CLASS_LABEL,
        CLASS_LABEL_TH,
        COMPARE,
        LABEL_LIST_SELECT,
        INPUT_SELECT,
        INPUT_SELECT_DEFAULT,
        LABEL_SHOW,
        LIMIT_ROW,
        PRODUCT_GRID,
        COUNT_PAGE,
        LIST_GROUP,
        COUNT_DESCTOP
    ]

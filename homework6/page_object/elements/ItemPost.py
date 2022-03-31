from selenium.webdriver.common.by import By


class ItemPost:
    TITLE_PAGE = (By.LINK_TEXT, "Desktops")
    PRODUCT = (By.XPATH, "//*[@id='product-product']//a[text()='Apple Cinema 30\"']")
    IMAGES_PRODUCT = (By.CSS_SELECTOR, "[class='image-additional']")
    IMAGES_PRODUCT_MAIN = (By.XPATH, "//*[@class='thumbnails']//img[@title='Apple Cinema 30\"']")
    TAB_DESCRIPTION = (By.XPATH, "//*[@class='nav nav-tabs']//a[text()='Description']")
    TAB_SPECIFICATION = (By.XPATH, "//*[@class='nav nav-tabs']//a[text()='Specification']")
    TAB_REVIEWS = (By.XPATH, "//*[@class='nav nav-tabs']//a[text()='Reviews (0)']")
    BUTTON_ADD_ITEM_COMPARE = (By.XPATH, "//*[@class='fa fa-heart']")
    BUTTON_ITEM_COMPARE = (By.XPATH, "//*[@class='fa fa-exchange']")
    TITLE_ITEM = (By.XPATH, "//*[@id='content']//*[text()='Apple Cinema 30\"']")
    ITEM_BRAND = (By.XPATH, "//*[@class='col-sm-4']//*[text()='Brand: ']")
    ITEM_PRICE = (By.XPATH, "//*[@class='col-sm-4']//h2[text()='$110.00']")
    ITEM_LABEL_AVAILABLE = (By.XPATH, "//*[@id='product']//*[text()='Available Options']")
    ITEM_RADIO = (By.XPATH, "//*[@id='product']//*[text()='Radio']")
    ITEM_CHECKBOX = (By.XPATH, "//*[@id='product']//*[text()='Checkbox']")
    ITEM_TEXT = (By.XPATH, "//input[@id='input-option208']")
    ITEM_SELECT_COLOUR = (By.CSS_SELECTOR, "[id='input-option217']>[value='3']")
    ITEM_TEXTAREA = (By.CSS_SELECTOR, "[id='input-option209']")
    ITEM_BUTTON_UPLOAD = (By.CSS_SELECTOR, "[id='button-upload222']")
    ITEM_DATE = (By.CSS_SELECTOR, "[id='input-option219']")
    ITEM_TIME = (By.CSS_SELECTOR, "[id='input-option221']")
    ITEM_DATE_TIME = (By.CSS_SELECTOR, "[id='input-option220']")
    ITEM_QUANTITY = (By.CSS_SELECTOR, "[id='input-quantity']")
    ITEM_ADD_TO_CART = (By.XPATH, "//*[@id='button-cart' and text()='Add to Cart']")
    TEXT_ALERT = (By.XPATH, "//*[@class='alert alert-info'][text()=' This product has a minimum quantity of 2']")

    locators = [
        TITLE_PAGE,
        PRODUCT,
        IMAGES_PRODUCT,
        IMAGES_PRODUCT_MAIN,
        TAB_DESCRIPTION,
        TAB_SPECIFICATION,
        TAB_REVIEWS,
        BUTTON_ADD_ITEM_COMPARE,
        BUTTON_ITEM_COMPARE,
        TITLE_ITEM,
        ITEM_BRAND,
        ITEM_PRICE,
        ITEM_LABEL_AVAILABLE,
        ITEM_RADIO,
        ITEM_CHECKBOX,
        ITEM_TEXT,
        ITEM_SELECT_COLOUR,
        ITEM_TEXTAREA,
        ITEM_BUTTON_UPLOAD,
        ITEM_DATE,
        ITEM_TIME,
        ITEM_DATE_TIME,
        ITEM_QUANTITY,
        ITEM_ADD_TO_CART,
        TEXT_ALERT
    ]

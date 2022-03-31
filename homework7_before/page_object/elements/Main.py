from selenium.webdriver.common.by import By


class Main:
    HEADER_BUTTON_CURRENCY = (By.CSS_SELECTOR, "button[class='btn btn-link dropdown-toggle']")
    HEADER_PHONE = (By.XPATH, "//span[text()='123456789']")
    HEADER_LK = (By.XPATH, "//span[text()='My Account']")
    MENU_REGISTER = (By.CSS_SELECTOR, "a[href*='register']")
    HEADER_WISH_LIST = (By.XPATH, "//span[text()='Wish List (0)']")
    HEADER_SHOPING_CART = (By.XPATH, "//span[text()='Shopping Cart']")
    HEADER_CHECKOUT = (By.XPATH, "//span[text()='Checkout']")
    SEARCH = (By.ID, "search")
    CART = (By.ID, "cart")
    LABEL_STORE = (By.LINK_TEXT, "Your Store")
    MENU_DESCTOPS = (By.LINK_TEXT, "Desktops")
    MENU_LAPTOPS = (By.LINK_TEXT, "Laptops & Notebooks")
    MENU_TABLETS = (By.LINK_TEXT, "Tablets")
    MENU_SOFTWARE = (By.LINK_TEXT, "Software")
    MENU_PHONES = (By.LINK_TEXT, "Phones & PDAs")
    MENU_CAMERAS = (By.LINK_TEXT, "Cameras")
    MENU_MP3 = (By.LINK_TEXT, "MP3 Players")
    CAROUSEL_MAIN = (By.CSS_SELECTOR, "img[src$='.jpg'][alt='iPhone 6']")
    TITLE_FEATURED_PATH = (By.CSS_SELECTOR, "#content > h3")
    TITLE_FEATURED = (By.XPATH, "//div[@id='content' and @class='col-sm-12']/h3[text()='Featured']")
    FEATURED_ADD_TO_CART = (By.XPATH, "//*[@id='content']//i[@class='fa fa-shopping-cart']")
    CAROUSEL = (By.XPATH, "//div[@id='carousel0']")
    FOOTER_INFORMATION = (By.XPATH, "//footer//h5[text()='Information']")
    FOOTER_CUSTOMER_SERVICE = (By.XPATH, "//footer//h5[text()='Customer Service']")
    FOOTER_EXTRAS = (By.XPATH, "//footer//h5[text()='Extras']")
    FOOTER_MY_ACCOUNT = (By.XPATH, "//footer//h5[text()='My Account']")
    FOOTER_POWERED_BY = (By.XPATH, "//footer//p[text()='Powered By ']")
    FOOTER_YOUR_STORE = (By.XPATH, "//footer//p[text()=' Your Store © 2022']")
    SELECT_EUR = (By.XPATH, "//*[@name='EUR']")
    CONFIRM_SELECT_EUR = (By.XPATH, "//*[@id='form-currency']//strong[text()='€']")

    locators = [
        HEADER_BUTTON_CURRENCY,
        HEADER_PHONE,
        HEADER_LK,
        HEADER_WISH_LIST,
        HEADER_SHOPING_CART,
        HEADER_CHECKOUT,
        SEARCH,
        CART,
        LABEL_STORE,
        MENU_DESCTOPS,
        MENU_LAPTOPS,
        MENU_TABLETS,
        MENU_SOFTWARE,
        MENU_PHONES,
        MENU_CAMERAS,
        MENU_MP3,
        CAROUSEL_MAIN,
        TITLE_FEATURED_PATH,
        TITLE_FEATURED,
        FEATURED_ADD_TO_CART,
        CAROUSEL,
        FOOTER_INFORMATION,
        FOOTER_CUSTOMER_SERVICE,
        FOOTER_EXTRAS,
        FOOTER_MY_ACCOUNT,
        FOOTER_POWERED_BY,
        FOOTER_YOUR_STORE
    ]

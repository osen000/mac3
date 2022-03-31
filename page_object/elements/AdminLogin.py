from selenium.webdriver.common.by import By


class AdminLogin:
    TITLE_ADMIN_PAGE = (By.CSS_SELECTOR, "[title='OpenCart']")
    NAME_ADMIN_PAGE = (By.CSS_SELECTOR, "[class='panel-title']>[class='fa fa-lock']")
    USERNNAME_PATH = (By.CSS_SELECTOR, "[for='input-username']")
    INPUT_USERNNAME = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD_CLASS = (By.CSS_SELECTOR, "[class='fa fa-user']")
    PASSWORD_PATH = (By.CSS_SELECTOR, "[for='input-password']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[name='password']")
    TITLE = (By.XPATH, "//*[@class='input-group-addon']/*[@class='fa fa-lock']")
    LINK_TEXT_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    SUBMIT_ENTER = (By.CSS_SELECTOR, "[type='submit']")
    LINK_TEXT_TITLE = (By.LINK_TEXT, "OpenCart")
    FOOTER_TEXT = (By.XPATH, "//*[@id='footer' and text()=' © 2009-2022 All Rights Reserved.']")
    PATH_TEXT_FOR_LOGIN = (By.XPATH, "//*[@id='content']//h1[text()='Dashboard']")

    locators = [
        TITLE_ADMIN_PAGE,
        NAME_ADMIN_PAGE,
        USERNNAME_PATH,
        INPUT_USERNNAME,
        PASSWORD_CLASS,
        PASSWORD_PATH,
        INPUT_PASSWORD,
        TITLE,
        LINK_TEXT_PASSWORD,
        SUBMIT_ENTER,
        LINK_TEXT_TITLE,
        FOOTER_TEXT
               ]

    locators_for_login = [
        INPUT_USERNNAME,
        INPUT_PASSWORD,
        SUBMIT_ENTER
    ]

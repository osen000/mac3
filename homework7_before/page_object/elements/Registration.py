from selenium.webdriver.common.by import By


class Registration:
    HOME_PAGE_PIC = (By.XPATH, "//*[@class='fa fa-home']")
    TAB_ACCOUNT = (By.LINK_TEXT, "Account")
    TAB_REGISTER = (By.LINK_TEXT, "Register")
    LABEL_REGISTER_ACCOUNT = (By.XPATH, "//*[@class='col-sm-9']/*[text()='Register Account']")
    PROMPT_REGISTER_ACCOUNT = (By.XPATH, "//*[@class='col-sm-9']/*[text()='If you already have an account with us, "
                                         "please login at the ']")
    HREF_LOGIN_PAGE = (By.XPATH, "//*[@class='col-sm-9']//*[text()='login page']")
    TITLE_PERSONAL_DETAILS = (By.XPATH, "//*[@id='account']/*[text()='Your Personal Details']")
    TITLE_FIRST_NAME = (By.XPATH, "//*[@for='input-firstname'][text()='First Name']")
    INPUT_FIRST_NAME = (By.XPATH, "//*[@id='input-firstname']")
    TITLE_LAST_NAME = (By.XPATH, "//*[@for='input-lastname'][text()='Last Name']")
    INPUT_LAST_NAME = (By.XPATH, "//*[@id='input-lastname']")
    TITLE_EMAIL = (By.XPATH, "//*[@for='input-email'][text()='E-Mail']")
    INPUT_EMAIL = (By.XPATH, "//*[@id='input-email']")
    TITLE_PHONE = (By.XPATH, "//*[@for='input-telephone'][text()='Telephone']")
    INPUT_PHONE = (By.XPATH, "//*[@id='input-telephone']")
    LABEL_PASSWORD = (By.XPATH, "//*[@id='content']//*[text()='Your Password']")
    TITLE_PASSWORD = (By.XPATH, "//*[@for='input-password'][text()='Password']")
    INPUT_PASSWORD = (By.XPATH, "//*[@id='input-password']")
    TITLE_PASSWORD_CONFIRM = (By.XPATH, "//*[@for='input-confirm'][text()='Password Confirm']")
    INPUT_PASSWORD_CONFIRM = (By.XPATH, "//*[@id='input-confirm']")
    LABEL_NEWSLETTER = (By.XPATH, "//*[@id='content']//*[text()='Newsletter']")
    TITLE_SUBSCRIBE = (By.XPATH, "//*[@id='content']//label[text()='Subscribe']")
    RADIO_YES = (By.XPATH, "//*[@class='radio-inline']/*[@value='1']")
    RADIO_NO = (By.XPATH, "//*[@class='radio-inline']/*[@value='0' and @checked='checked']")
    TEXT_AGREE = (By.XPATH, "//*[@class='pull-right'][text()='I have read and agree to the ']")
    TEXT_PRIVACY_POLICY = (By.XPATH, "//*[@class='agree']/*[text()='Privacy Policy']")
    CHECKBOX_PRIVACY_POLICY = (By.CSS_SELECTOR, "[type='checkbox'][name='agree']")
    SUBMIT_CONTINUE = (By.CSS_SELECTOR, "[type='submit'][value='Continue']")
    MENU_RIGHT = (By.CSS_SELECTOR, "[class='list-group-item']")
    MENU_RIGHT_LOGIN = (By.XPATH, "//*[@class='list-group-item'][text()='Login']")
    MENU_RIGHT_REGISTER = (By.XPATH, "//*[@class='list-group-item'][text()='Register']")
    MENU_RIGHT_FORGOTTEN_PASSWORD = (By.XPATH, "//*[@class='list-group-item'][text()='Forgotten Password']")
    MENU_RIGHT_MY_ACCOUNT = (By.XPATH, "//*[@class='list-group-item'][text()='My Account']")
    MENU_RIGHT_ADDRESS_BOOK = (By.XPATH, "//*[@class='list-group-item'][text()='Address Book']")
    MENU_RIGHT_WISH_LIST = (By.XPATH, "//*[@class='list-group-item'][text()='Wish List']")
    MENU_RIGHT_ORDER_HISTORY = (By.XPATH, "//*[@class='list-group-item'][text()='Order History']")
    MENU_RIGHT_DOWNLOADS = (By.XPATH, "//*[@class='list-group-item'][text()='Downloads']")
    MENU_RIGHT_PAYMENTS = (By.XPATH, "//*[@class='list-group-item'][text()='Recurring payments']")
    MENU_RIGHT_REWARD_POINTS = (By.XPATH, "//*[@class='list-group-item'][text()='Reward Points']")
    MENU_RIGHT_RETURNS = (By.XPATH, "//*[@class='list-group-item'][text()='Returns']")
    MENU_RIGHT_TRANSACTIONS = (By.XPATH, "//*[@class='list-group-item'][text()='Transactions']")
    MENU_RIGHT_NEWSLETTER = (By.XPATH, "//*[@class='list-group-item'][text()='Newsletter']")
    NEW_USER_CONFIRM = (By.XPATH, "//*[@id='content']/h1[text()='Your Account Has Been Created!']")

    locators = [
        HOME_PAGE_PIC,
        TAB_ACCOUNT,
        TAB_REGISTER,
        LABEL_REGISTER_ACCOUNT,
        PROMPT_REGISTER_ACCOUNT,
        HREF_LOGIN_PAGE,
        TITLE_PERSONAL_DETAILS,
        TITLE_FIRST_NAME,
        INPUT_FIRST_NAME,
        TITLE_LAST_NAME,
        INPUT_LAST_NAME,
        TITLE_EMAIL,
        INPUT_EMAIL,
        TITLE_PHONE,
        INPUT_PHONE,
        LABEL_PASSWORD,
        TITLE_PASSWORD,
        INPUT_PASSWORD,
        TITLE_PASSWORD_CONFIRM,
        INPUT_PASSWORD_CONFIRM,
        LABEL_NEWSLETTER,
        TITLE_SUBSCRIBE,
        RADIO_YES,
        RADIO_NO,
        TEXT_AGREE,
        TEXT_PRIVACY_POLICY,
        CHECKBOX_PRIVACY_POLICY,
        SUBMIT_CONTINUE,
        MENU_RIGHT,
        MENU_RIGHT_LOGIN,
        MENU_RIGHT_REGISTER,
        MENU_RIGHT_FORGOTTEN_PASSWORD,
        MENU_RIGHT_MY_ACCOUNT,
        MENU_RIGHT_ADDRESS_BOOK,
        MENU_RIGHT_WISH_LIST,
        MENU_RIGHT_ORDER_HISTORY,
        MENU_RIGHT_DOWNLOADS,
        MENU_RIGHT_PAYMENTS,
        MENU_RIGHT_REWARD_POINTS,
        MENU_RIGHT_RETURNS,
        MENU_RIGHT_TRANSACTIONS,
        MENU_RIGHT_NEWSLETTER
    ]

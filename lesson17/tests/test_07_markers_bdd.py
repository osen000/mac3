import allure


@allure.epic("2021Q3")
@allure.feature("Authorization")
@allure.story("Valid credentials")
def test_auth_valid():
    pass


@allure.epic("2021Q3")
@allure.feature("Authorization")
@allure.story("Invalid credentials")
def test_auth_non_valid():
    pass


@allure.epic("2021Q4")
@allure.feature("Export")
@allure.story("CSV")
def test_csv_export():
    pass

import allure


@allure.link('https://www.youtube.com/watch?v=7KgihdKTWY4')
def test_with_link():
    pass


@allure.link('https://www.youtube.com/watch?v=7KgihdKTWY4', name='Click me')
def test_with_named_link():
    pass


@allure.issue('140', name='Pytest-flaky test retries shows like test steps')
def test_with_issue_link():
    pass


@allure.testcase('150', 'Test case title')
def test_with_testcase_link():
    pass

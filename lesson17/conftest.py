import allure
import os
import pytest


@allure.step('step in conftest.py')
def conftest_step():
    pass


@pytest.fixture
def fixture_conftest_step():
    conftest_step()


@pytest.fixture(scope="session", autouse=True)
def get_environment(pytestconfig):
    props = {
        'Browser': 'Chrome',
        'Browser.Version': '98.0',
        'Stand': 'Production',
        'Shell': os.getenv('SHELL')
    }

    tests_root = pytestconfig.rootdir
    with open(f'{tests_root}/allure-results/environment.properties', 'w') as f:
        env_props = '\n'.join([f'{k}={v}' for k, v in props.items()])
        f.write(env_props)

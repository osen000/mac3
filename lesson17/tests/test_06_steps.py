import allure

from .steps import imported_step


@allure.step
def passing_step():
    pass


@allure.step("Root step")
def step_with_nested_steps():
    nested_step()


@allure.step
def nested_step():
    nested_step_with_arguments(1, 'abc')


@allure.step("Nested step with args: {0}, {1}")
def nested_step_with_arguments(arg1, arg2):
    pass


def test_with_imported_step():
    passing_step()
    imported_step()


def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()


def test_with_step_in_fixture(fixture_conftest_step):
    passing_step()


def test_step_context_manager():
    var = 1
    with allure.step(f"Context manager step with arg: {var}"):
        print(var)

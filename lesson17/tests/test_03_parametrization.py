import pytest


@pytest.fixture(params=[0, 1])
def func_params():
    pass


@pytest.mark.parametrize("x", [0, 1])
def test_x(x):
    pass


def test_params(func_params):
    pass


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [0, 1])
def test_both(func_params, x, y):
    pass

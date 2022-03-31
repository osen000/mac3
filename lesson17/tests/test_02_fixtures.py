import pytest


@pytest.fixture(scope="session")
def session():
    print("Init session fixt")
    yield
    print("Clean up session fixt")


@pytest.fixture(scope="function")
def func():
    print("Init func fixt")
    yield
    print("Clean up func fixt")


def test_1(session, func):
    print("Run test_1")


def test_2():
    print("Run test_2")


def test_3(func):
    print("Run test_3")


def test_4(session):
    print("Run test_4")

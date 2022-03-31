import pytest

from src.Hero import Hero


@pytest.fixture
def default_hero():
    hero = Hero(defend=30, healing=30, power=40, name="Ninja")
    yield hero
    del hero


@pytest.fixture
def second_hero():
    hero = Hero(defend=30, healing=40, power=30, name="Optimus")
    yield hero
    del hero

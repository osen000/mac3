import pytest
import random

from src.Hero import Hero


def test_hero_creation():
    """Check creating hero with sum of attributes > 100"""
    with pytest.raises(AttributeError):
        Hero(defend=30, healing=30, power=70, name="Ninja")


def test_hero_hit_negative(default_hero):
    """Hero can't hit other classes"""

    class Car:
        pass

    with pytest.raises(Exception):
        default_hero.hit(Car())


def test_hit(default_hero, second_hero):
    """Hero hit other hero and make damage"""
    default_hero.hit(second_hero)
    assert second_hero.health == 90


def test_heal_health_increase(default_hero, second_hero):
    """Healing can't increase health over 100"""
    default_hero.hit(second_hero)
    assert second_hero.health == 90
    second_hero.heal()
    assert second_hero.health == 100


def test_heal_hero_full_health(default_hero):
    """Full health is not healing for hero"""
    assert default_hero.heal() == "Hero health is full"
    assert default_hero.health == 100


# Тесты ниже работают плохо так если есть сложная зависимость от состоятния класса.
def test_hero_counter():
    random_amount = random.randint(5, 10)
    heroes = []
    for i in range(random_amount):
        heroes.append(Hero(defend=30, healing=30, power=40, name=f"Hero{i}"))
    assert heroes[0].count == random_amount


def test_hero_counter_delete():
    heroes = []
    for i in range(5):
        heroes.append(Hero(defend=30, healing=30, power=40, name=f"Hero{i}"))
    assert heroes[0].count == 5, "There should be 5 heroes"
    del heroes[0]
    assert heroes.pop().count == 4, "There should be only 4 heroes in count"

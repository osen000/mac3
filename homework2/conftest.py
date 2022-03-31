import pytest
from homework2.Rectangle import Rectangle
from homework2.Square import Square
from homework2.Circle import Circle
from homework2.Triangle import Triangle


@pytest.fixture
def create_rectangle():
    return Rectangle(10, 20)


@pytest.fixture
def create_square():
    return Square(10)


@pytest.fixture
def create_circle():
    return Circle(10)


@pytest.fixture
def create_triangle():
    return Triangle(3, 4, 5)


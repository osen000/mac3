from src.Figure import Figure
import math


class Circle(Figure):
    name = 'circle'

    def __init__(self, radius):
        Figure.__init__(self)
        # self.name = 'Circle'
        self.radius = radius
        self.area = 0
        self.perimeter = 0

    def calculate_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return self.perimeter

    def calculate_area(self):
        self.area = math.pi * (self.radius ** 2)
        return self.area

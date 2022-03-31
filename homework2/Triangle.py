from src.Figure import Figure
import math


class Triangle(Figure):
    name = 'triangle'

    def __init__(self, line1, line2, line3):
        Figure.__init__(self)
        self.name = 'triangle'
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.area = 0
        self.perimeter = 0

    def calculate_perimeter(self):
        self.perimeter = self.line1 + self.line2 + self.line3
        return self.perimeter

    def calculate_area(self):
        p_perimeter = (self.line1 + self.line2 + self.line3) / 2
        self.area = math.sqrt(p_perimeter * (p_perimeter - self.line1) * (p_perimeter - self.line2) * (p_perimeter -
                                                                                                       self.line3))

        return self.area

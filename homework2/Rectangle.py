from src.Figure import Figure


class Rectangle(Figure):
    name = 'rectangle'

    def __init__(self, line1, line2):
        Figure.__init__(self)
        self.line1 = line1
        self.line2 = line2
        self.area = 0
        self.perimeter = 0

    def calculate_perimeter(self):
        self.perimeter = (self.line1 + self.line2) * 2
        return self.perimeter

    def calculate_area(self):
        self.area = self.line1 * self.line2
        return self.area

from src.Figure import Figure


class Square(Figure):
    name = 'square'

    def __init__(self, line):
        Figure.__init__(self)
        self.name = 'square'
        self.line = line
        self.area = 0
        self.perimeter = 0

    def calculate_perimeter(self):
        self.perimeter = self.line * 4
        return self.perimeter

    def calculate_area(self):
        self.area = self.line ** 2
        return self.area


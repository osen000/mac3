

class Figure:

    def __init__(self):
        self.perimeter = 0
        self.area = 0
        self.names = ['triangle', 'square', 'rectangle', 'circle']

    def calculate_perimeter(self):
        return self.perimeter

    def calculate_area(self):
        return self.area

    def add_area(self, figure):
        if figure.name in self.names:
            return self.calculate_area() + figure.calculate_area()
        else:
            raise ValueError('Передан неправильный класс')

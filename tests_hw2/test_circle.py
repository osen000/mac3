class TestSquare:
    def test_area(self, create_circle):
        assert create_circle.calculate_area() == 314.1592653589793

    def test_area_error(self, create_circle):
        assert create_circle.calculate_area() != 314

    def test_perimeter(self, create_circle):
        assert create_circle.calculate_perimeter() == 62.83185307179586

    def test_perimeter_error(self, create_circle):
        assert create_circle.calculate_perimeter() != 62

    def test_add_area_triangle(self, create_circle, create_triangle):
        assert create_circle.add_area(create_triangle) == 320.1592653589793

    def test_add_area_rectangle(self, create_circle, create_rectangle):
        assert create_circle.add_area(create_rectangle) == 514.1592653589794

    def test_add_area_square(self, create_circle, create_square):
        assert create_circle.add_area(create_square) == 414.1592653589793

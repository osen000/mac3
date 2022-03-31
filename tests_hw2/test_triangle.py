class TestRectangle:
    def test_area(self, create_triangle):
        assert create_triangle.calculate_area() == 6

    def test_area_error(self, create_triangle):
        assert create_triangle.calculate_area() != 7

    def test_perimeter(self, create_triangle):
        assert create_triangle.calculate_perimeter() == 12

    def test_perimeter_error(self, create_triangle):
        assert create_triangle.calculate_perimeter() != 13

    def test_add_area_square(self, create_triangle, create_square):
        assert create_triangle.add_area(create_square) == 106.0

    def test_add_area_circle(self, create_triangle, create_circle):
        assert create_triangle.add_area(create_circle) == 320.1592653589793

    def test_add_area_rectangle(self, create_triangle, create_rectangle):
        assert create_triangle.add_area(create_rectangle) == 206.0

class TestRectangle:
    def test_area(self, create_rectangle):
        assert create_rectangle.calculate_area() == 200

    def test_area_error(self, create_rectangle):
        assert create_rectangle.calculate_area() != 201

    def test_perimeter(self, create_rectangle):
        assert create_rectangle.calculate_perimeter() == 60

    def test_perimeter_error(self, create_rectangle):
        assert create_rectangle.calculate_perimeter() != 61

    def test_add_area_triangle(self, create_rectangle, create_triangle):
        assert create_rectangle.add_area(create_triangle) == 206

    def test_add_area_circle(self, create_rectangle, create_circle):
        assert create_rectangle.add_area(create_circle) == 514.1592653589794

    def test_add_area_square(self, create_rectangle, create_square):
        assert create_rectangle.add_area(create_square) == 300

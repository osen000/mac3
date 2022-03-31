class TestSquare:
    def test_area(self, create_square):
        assert create_square.calculate_area() == 100

    def test_area_error(self, create_square):
        assert create_square.calculate_area() != 101

    def test_perimeter(self, create_square):
        assert create_square.calculate_perimeter() == 40

    def test_perimeter_error(self, create_square):
        assert create_square.calculate_perimeter() != 41

    def test_add_area_triangle(self, create_square, create_triangle):
        assert create_square.add_area(create_triangle) == 106.0

    def test_add_area_circle(self, create_square, create_circle):
        assert create_square.add_area(create_circle) == 414.1592653589793

    def test_add_area_rectangle(self, create_square, create_rectangle):
        assert create_square.add_area(create_rectangle) == 300

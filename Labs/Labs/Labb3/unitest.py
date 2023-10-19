import unittest
from Geometry import Geometry
from circle import Circle
from rectangle import Rectangle
from sphere import Sphere
from cube import Cube

class TestGeometry(unittest.TestCase):
    """
    Unit testing for the Geometry class (the base class).
    """
    def setUp(self):
        """
        Set up test data for the Geometry class.
        """
        self.geometry = Geometry(0, 0)

    def test_create_geometry(self):
        """
        Test creating a Geometry instance.
        """
        self.assertIsInstance(self.geometry, Geometry)

    def test_geometry_area(self):
        """
        Test area calculation for the Geometry class.
        This should always raise a NotImplementedError.
        """
        with self.assertRaises(NotImplementedError):
            self.geometry.area()

    def test_geometry_circumference(self):
        """
        Test circumference calculation for the Geometry class.
        This should always raise a NotImplementedError.
        """
        with self.assertRaises(NotImplementedError):
            self.geometry.circumference()

    def test_geometry_center_point(self):
        """
        Test center point calculation for the Geometry class.
        This should return the initial point (0, 0).
        """
        center = self.geometry.center_point()
        self.assertEqual(center, (0, 0))

    def test_geometry_move_geometry(self):
        """
        Test moving the Geometry instance to a new point.
        """
        self.geometry.move_geometry(1, 2)
        center = self.geometry.center_point()
        self.assertEqual(center, (1, 2))

    def test_geometry_check_position(self):
        """
        Test checking the position of a point with respect to the Geometry.
        This should always raise a NotImplementedError.
        """
        with self.assertRaises(NotImplementedError):
            self.geometry.check_position(1, 2)

    def test_geometry_is_inside(self):
        """
        Test checking if a point is inside the Geometry.
        This should always raise a NotImplementedError.
        """
        with self.assertRaises(NotImplementedError):
            self.geometry.is_inside(1, 2)

    def test_geometry_validate_length(self):
        """
        Test validating length for the Geometry class.
        This should raise a ValueError for negative values.
        """
        with self.assertRaises(ValueError):
            Geometry.validate_length(-1)
        self.assertTrue(True)  
        
    def test_geometry_validate_real_numbers(self):
        """
        Test validating real numbers for the Geometry class.
        This should raise a TypeError for non-integer and non-float values.
        """
        with self.assertRaises(TypeError):
            Geometry.validate_real_numbers("a")
        self.assertTrue(True)  

class TestCircle(unittest.TestCase):
    """
    Unit testing for the Circle class.
    """
    def setUp(self):
        """
        Set up test data for the Circle.
        """
        self.radius, self.x, self.y = 5, 1, 3
        self.circle = Circle(self.radius, self.x, self.y)

    def test_create_circle(self):
        """
        Test creating a Circle instance.
        """
        self.assertIsInstance(self.circle, Circle)

    def test_area(self):
        """
        Test calculating the area of a Circle.
        """
        self.assertAlmostEqual(self.circle.area(), 78.53981633974483)

class TestRectangle(unittest.TestCase):
    """
    Unit testing for the Rectangle class.
    """
    def setUp(self):
        """
        Set up test data for the Rectangle.
        """
        self.width, self.height, self.x, self.y = 4, 3, 4, 6
        self.rectangle = Rectangle(self.width, self.height, self.x, self.y)
        
    def test_create_rectangle(self):
        """
        Test creating a Rectangle instance.
        """
        self.assertIsInstance(self.rectangle, Rectangle)

    def test_area(self):
        """
        Test calculating the area of a Rectangle.
        """
        self.assertAlmostEqual(self.rectangle.area(), 12.0)

if __name__ == "__main":
    unittest.main()
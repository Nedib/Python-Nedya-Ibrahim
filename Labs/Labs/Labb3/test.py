import unittest
from Circle import Circle
from rectangle import Rectangle
from sphere import Sphere
from cube import Cube

class Circle(unittest.TestCase):
    """
    Unit testing for the Circle class.
    """
    def setUp(self):
        """
        Set up test data for the Circle.
        """
        self.radius, self.x, self.y = 5, 1, 3

    def create_circle(self):
        """
        Create a Circle instance.
        """
        return Circle(self.radius, self.x, self.y)

    def test_create_circle(self):
        """
        Test creating a Circle.
        """
        c1 = self.create_circle()
        c2 = Circle(5, 1, 3)
        self.assertEqual(c1, c2)

    def test_create_empty_circle(self):
        """
        Test creating an empty Circle (expecting an exception).
        """
        with self.assertRaises(TypeError):
            c = Circle()

    def test_create_invalid_circle(self):
        """
        Test creating a Circle with invalid arguments (expecting an exception).
        """
        with self.assertRaises(TypeError):
            c = Circle(5, 1, "a")

    def test_two_circle_not_equal(self):
        """
        Test that two Circle instances are not equal.
        """
        c1 = self.create_circle()
        c2 = Circle(1, 2, 7)
        self.assertNotEqual(c1, c2)

    def test_circle_minus_radius(self):
        """
        Test creating a Circle with a negative radius (expecting an exception).
        """
        with self.assertRaises(ValueError):
            c = Circle(-1, 2, 7)

    def test_area(self):
        """
        Test calculating the area of a Circle.
        """
        c1 = self.create_circle()
        self.assertAlmostEqual(c1.area(), 78.53981633974483)

class Sphere(unittest.TestCase):
    """
    Unit testing for the Sphere class.
    """
    def setUp(self):
        """
        Set up test data for the Sphere.
        """
        self.radius, self.x, self.y, self.z = 3, 2, 4, 2

    def create_sphere(self):
        """
        Create a Sphere instance.
        """
        return Sphere(self.radius, self.x, self.y, self.z)

    def test_create_sphere(self):
        """
        Test creating a Sphere.
        """
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 4, 2)
        self.assertEqual(s1, s2)

    def test_create_empty_sphere(self):
        """
        Test creating an empty Sphere (expecting an exception).
        """
        with self.assertRaises(TypeError):
            s = Sphere()

    def test_create_invalid_sphere(self):
        """
        Test creating a Sphere with invalid arguments (expecting an exception).
        """
        with self.assertRaises(TypeError):
            s = Sphere(5, 1, 2, "a")

    def test_two_sphere_not_equal(self):
        """
        Test that two Sphere instances are not equal.
        """
        s1 = self.create_sphere()
        s2 = Sphere(4, 2, 5, 4)
        self.assertNotEqual(s1, s2)

    def test_sphere_minus_radius(self):
        """
        Test creating a Sphere with a negative radius (expecting an exception).
        """
        with self.assertRaises(ValueError):
            s = Sphere(-1, 2, 3, 4)

    def test_area(self):
        """
        Test calculating the area of a Sphere.
        """
        s1 = self.create_sphere()
        self.assertAlmostEqual(s1.area(), 113.09733552923256)

class Rectangle(unittest.TestCase):
    """
    Unit testing for the Rectangle class.
    """
    def setUp(self):
        """
        Set up test data for the Rectangle.
        """
        self.side1, self.side2, self.x, self.y = 4, 3, 4, 6

    def create_rectangle(self):
        """
        Create a Rectangle instance.
        """
        return Rectangle(self.side1, self.side2, self.x, self.y)

    def test_create_rectangle(self):
        """
        Test creating a Rectangle.
        """
        r1 = self.create_rectangle()
        r2 = Rectangle(4, 3, 4, 6)
        self.assertEqual(r1, r2)

    def test_create_empty_rectangle(self):
        """
        Test creating an empty Rectangle (expecting an exception).
        """
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_create_invalid_rectangle(self):
        """
        Test creating a Rectangle with invalid arguments (expecting an exception).
        """
        with self.assertRaises(TypeError):
            r = Rectangle(5, 4, 1, "a")

    def test_two_rectangle_not_equal(self):
        """
        Test that two Rectangle instances are not equal.
        """
        r1 = self.create_rectangle()
        r2 = Rectangle(10, 2, 3, -7)
        self.assertNotEqual(r1, r2)

    def test_rectangle_minus_length(self):
        """
        Test creating a Rectangle with a negative length (expecting an exception).
        """
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 3, 2, 7)

    def test_area(self):
        """
        Test calculating the area of a Rectangle.
        """
        r1 = self.create_rectangle()
        self.assertAlmostEqual(r1.area(), 12.0)

class Cube(unittest.TestCase):
    """
    Unit testing for the Cube class.
    """
    def setUp(self):
        """
        Set up test data for the Cube.
        """
        self.side, self.x, self.y, self.z = 4, 3, 4, 2

    def create_cube(self):
        """
        Create a Cube instance.
        """
        return Cube(self.side, self.x, self.y, self.z)

    def test_create_cube(self):
        """
        Test creating a Cube.
        """
        c1 = self.create_cube()
        c2 = Cube(4, 3, 4, 2)
        self.assertEqual(c1, c2)

    def test_create_empty_cube(self):
        """
        Test creating an empty Cube (expecting an exception).
        """
        with self.assertRaises(TypeError):
            c = Cube()

    def test_create_invalid_cube(self):
        """
        Test creating a Cube with invalid arguments (expecting an exception).
        """
        with self.assertRaises(TypeError):
            c = Cube(5, 4, 1, "a")

    def test_two_cube_not_equal(self):
        """
        Test that two Cube instances are not equal.
        """
        c1 = self.create_cube()
        c2 = Cube(2, 2, 3, -7)
        self.assertNotEqual(c1, c2)

    def test_cube_minus_length(self):
        """
        Test creating a Cube with a negative length (expecting an exception).
        """
        with self.assertRaises(ValueError):
            c = Cube(-1, 3, 2, 7)

    def test_cube_volume(self):
        """
        Test calculating the volume of a Cube.
        """
        c1 = self.create_cube()
        self.assertAlmostEqual(c1.volume(), 64)

    def test_cube_circumradius(self):
        """
        Test calculating the circumradius of a Cube.
        """
        c1 = self.create_cube()
        self.assertAlmostEqual(c1.circumradius(), 3.4641016151377546)

if __name__ == "__main":
    unittest.main()
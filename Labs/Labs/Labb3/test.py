import unittest
from Circle import Circle
from rectangle import Rectangle
from sphere import Sphere
from cube import Cube

class Circle(unittest.TestCase):
    def setUp(self):
        self.radius, self.x, self.y = 5, 1, 3

    def create_circle(self):
        return Circle(self.radius, self.x, self.y)

    def test_create_circle(self):
        c1 = self.create_circle()
        c2 = Circle(5, 1, 3)
        self.assertEqual(c1, c2)

    def test_create_empty_circle(self):
        with self.assertRaises(TypeError):
            c = Circle()

    def test_create_invalid_circle(self):
        with self.assertRaises(TypeError):
            c = Circle(5, 1, "a")

    def test_two_circle_not_equal(self):
        c1 = self.create_circle()
        c2 = Circle(1, 2, 7)
        self.assertNotEqual(c1, c2)

    def test_circle_minus_radius(self):
        with self.assertRaises(ValueError):
            c = Circle(-1, 2, 7)

    def test_area(self):
        c1 = self.create_circle()
        self.assertAlmostEqual(c1.area(), 78.53981633974483)

class Sphere(unittest.TestCase):
    def setUp(self):
        self.radius, self.x, self.y, self.z = 3, 2, 4, 2

    def create_sphere(self):
        return Sphere(self.radius, self.x, self.y, self.z)

    def test_create_sphere(self):
        s1 = self.create_sphere()
        s2 = Sphere(3, 2, 4, 2)
        self.assertEqual(s1, s2)

    def test_create_empty_sphere(self):
        with self.assertRaises(TypeError):
            s = Sphere()

    def test_create_invalid_sphere(self):
        with self.assertRaises(TypeError):
            s = Sphere(5, 1, 2, "a")

    def test_two_sphere_not_equal(self):
        s1 = self.create_sphere()
        s2 = Sphere(4, 2, 5, 4)
        self.assertNotEqual(s1, s2)

    def test_sphere_minus_radius(self):
        with self.assertRaises(ValueError):
            s = Sphere(-1, 2, 3, 4)

    def test_area(self):
        s1 = self.create_sphere()
        self.assertAlmostEqual(s1.area(), 113.09733552923256)

class Rectangle(unittest.TestCase):
    def setUp(self):
        self.side1, self.side2, self.x, self.y = 4, 3, 4, 6

    def create_rectangle(self):
        return Rectangle(self.side1, self.side2, self.x, self.y)

    def test_create_rectangle(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(4, 3, 4, 6)
        self.assertEqual(r1, r2)

    def test_create_empty_rectangle(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_create_invalid_rectangle(self):
        with self.assertRaises(TypeError):
            r = Rectangle(5, 4, 1, "a")

    def test_two_rectangle_not_equal(self):
        r1 = self.create_rectangle()
        r2 = Rectangle(10, 2, 3, -7)
        self.assertNotEqual(r1, r2)

    def test_rectangle_minus_length(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 3, 2, 7)

    def test_area(self):
        r1 = self.create_rectangle()
        self.assertAlmostEqual(r1.area(), 12.0)

class Cube(unittest.TestCase):
    def setUp(self):
        self.side, self.x, self.y, self.z = 4, 3, 4, 2

    def create_cube(self):
        return Cube(self.side, self.x, self.y, self.z)

    def test_create_cube(self):
        c1 = self.create_cube()
        c2 = Cube(4, 3, 4, 2)
        self.assertEqual(c1, c2)

    def test_create_empty_cube(self):
        with self.assertRaises(TypeError):
            c = Cube()

    def test_create_invalid_cube(self):
        with self.assertRaises(TypeError):
            c = Cube(5, 4, 1, "a")

    def test_two_cube_not_equal(self):
        c1 = self.create_cube()
        c2 = Cube(2, 2, 3, -7)
        self.assertNotEqual(c1, c2)

    def test_cube_minus_length(self):
        with self.assertRaises(ValueError):
            c = Cube(-1, 3, 2, 7)

    def test_cube_volume(self):
        c1 = self.create_cube()
        self.assertAlmostEqual(c1.volume(), 64)

    def test_cube_circumradius(self):
        c1 = self.create_cube()
        self.assertAlmostEqual(c1.circumradius(), 3.4641016151377546)

if __name__ == "__main":
    unittest.main()
import unittest
from circle import Circle
from rectangle import Rectangle
from sphere import Sphere
from cube import Cube

class TestGeometry(unittest.TestCase):
    def setUp(self):
        # Create instances of different geometric shapes for testing
        self.circle = Circle(5, 1, 3)
        self.sphere = Sphere(3, 2, 4, 2)
        self.rectangle = Rectangle(4, 6, 3, 4)
        self.cube = Cube(2, 4, 3, 2)

    def test_circle_area(self):
        """Test the area calculation for a Circle."""
        self.assertAlmostEqual(self.circle.area(), 78.53981633974483)

    def test_sphere_area(self):
        """Test the surface area calculation for a Sphere."""
        self.assertAlmostEqual(self.sphere.area(), 113.09733552923256)

    def test_sphere_volume(self):
        """Test the volume calculation for a Sphere."""
        self.assertAlmostEqual(self.sphere.volume(), 113.09733552923256)

    def test_rectangle_area(self):
        """Test the area calculation for a Rectangle."""
        self.assertEqual(self.rectangle.area(), 24.0)

    def test_cube_volume(self):
        """Test the volume calculation for a Cube."""
        self.assertAlmostEqual(self.cube.volume(), 8.0)

    def test_cube_circumradius(self):
        """Test the circumradius calculation for a Cube."""
        self.assertAlmostEqual(self.cube.circumradius(), 1.7320508075688772)

    def test_circle_equality(self):
        """Test equality of two Circle instances."""
        other_circle = Circle(5, 1, 3)
        self.assertEqual(self.circle, other_circle)

    def test_sphere_equality(self):
        """Test equality of two Sphere instances."""
        other_sphere = Sphere(3, 2, 4, 2)
        self.assertEqual(self.sphere, other_sphere)

    def test_rectangle_equality(self):
        """Test equality of two Rectangle instances."""
        other_rectangle = Rectangle(4, 6, 3, 4)
        self.assertEqual(self.rectangle, other_rectangle)

    def test_cube_equality(self):
        """Test equality of two Cube instances."""
        other_cube = Cube(2, 4, 3, 2)
        self.assertEqual(self.cube, other_cube)

    def test_circle_inequality(self):
        """Test inequality of two Circle instances."""
        other_circle = Circle(1, 2, 7)
        self.assertNotEqual(self.circle, other_circle)

    def test_sphere_inequality(self):
        """Test inequality of two Sphere instances."""
        other_sphere = Sphere(4, 2, 5, 4)
        self.assertNotEqual(self.sphere, other_sphere)

    def test_rectangle_inequality(self):
        """Test inequality of two Rectangle instances."""
        other_rectangle = Rectangle(10, 2, 3, -7)
        self.assertNotEqual(self.rectangle, other_rectangle)

    def test_cube_inequality(self):
        """Test inequality of two Cube instances."""
        other_cube = Cube(2, 2, 3, -7)
        self.assertNotEqual(self.cube, other_cube)

if __name__ == "__main__":
    unittest.main()

"""The unittest code defines test cases to verify the correctness of geometric
 shape calculations and properties for circles, rectangles, spheres, and cubes"""


import unittest #Import necessary classes for geometric shapes from modules
from circle import Circle  
from rectangle_labb3 import Rectangle  
from sphere import Sphere  
from cube import Cube 

"""Initialize instances of geometric shapes with specified parameters
These parameters are the radius, dimensions, and position of the shapes
Some parameter values have been corrected here"""
class TestGeometry(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(5, 1, 3)  # Create a Circle instance with radius 5 and position (1, 3)
        self.sphere = Sphere(3, 2, 4, 2)  # Create a Sphere instance with radius 3 and position (2, 4, 2)
        self.rectangle = Rectangle(4, 6, 3, 4)  # Create a Rectangle instance with dimensions (4, 6) and position (3, 4)
        self.cube = Cube(2, 4, 3, 2)  # Create a Cube instance with side length 2 and position (4, 3, 2)

    """Test the properties of the Circle instance
    specifically, check if the area of the Circle is equal to the expected value"""
    def test_circle(self):
        self.assertEqual(self.circle.area(), 78.53981633974483)

    """Test the properties of the Sphere instance
        Check if the area and volume of the Sphere are approximately equal to expected values"""
    def test_sphere(self):
        self.assertAlmostEqual(self.sphere.area(), 113.09733552923256)
        self.assertAlmostEqual(self.sphere.volume(), 113.09733552923256)

    """Test the properties of the Rectangle instance
        Check if the area of the Rectangle is equal to the expected value"""
    def test_rectangle(self):
        self.assertEqual(self.rectangle.area(), 24.0)
        
    """Test the properties of the Cube instance
        Check if the volume and circumradius of the Cube are approximately equal to expected values"""
    def test_cube(self):
        self.assertAlmostEqual(self.cube.volume(), 8.0)
        self.assertAlmostEqual(self.cube.circumradius(), 1.7320508075688772)

if __name__ == "__main__": # If the script is executed directly, run the tests
    unittest.main()
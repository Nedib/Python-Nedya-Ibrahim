import math
import randompoint  
import matplotlib.pyplot as plt
from Geometry import Geometry  

# Generate random coordinates
point_x, point_y, point_z = randompoint.random_point()

class Circle:
    def __init__(self, radius, x, y):
        """
        Initialize a Circle with a given radius and center coordinates (x, y).

        :param radius: The radius of the circle (must be a positive number).
        :param x: The x-coordinate of the center.
        :param y: The y-coordinate of the center.
        """
        self.radius = radius
        self.x = x
        self.y = y
        Circle.validate_length(radius)
        Circle.validate_real_numbers(radius, x, y)

    @property
    def area(self):
        """
        Calculate and return the area of the circle.
        """
        return math.pi * self.radius ** 2

    @property
    def circumference(self):
        """
        Calculate and return the circumference of the circle.
        """
        return 2 * math.pi * self.radius

    def center_point(self):
        """
        Get the center point of the circle as a tuple (x, y).
        """
        return self.x, self.y

    def move_geometry(self, new_x, new_y):
        """
        Move the circle to a new center point with coordinates (new_x, new_y).

        :param new_x: The new x-coordinate.
        :param new_y: The new y-coordinate.
        """
        self.x = new_x
        self.y = new_y

    def check_position(self, point_x, point_y):
        """
        Check if a point with coordinates (point_x, point_y) is within the circle.

        :param point_x: The x-coordinate of the point.
        :param point_y: The y-coordinate of the point.
        :return: True if the point is within the circle, otherwise False.
        """
        d2 = (point_x - self.x) ** 2 + (point_y - self.y) ** 2
        return d2 <= self.radius ** 2

    @staticmethod
    def validate_length(value):
        """
        Validate that a value is a positive number (length or radius).

        :param value: The value to validate.
        :raises ValueError: If the value is not positive.
        """
        if value <= 0:
            raise ValueError(f"Length must be > 0, not {value}")
        Circle.validate_real_numbers(value)

    @staticmethod
    def validate_real_numbers(*values):
        """
        Validate that a list of values are either integers or floats.

        :param values: The values to validate.
        :raises TypeError: If any of the values is not an int or float.
        """
        for val in values:
            if not isinstance(val, (int, float)):
                raise TypeError(f"Values must be int or float, not {type(val)}")

    def __eq__(self, other):
        """
        Compare the radius of this circle with another circle.

        :param other: The other Circle object to compare with.
        :return: True if the radii are equal, otherwise False.
        """
        if isinstance(other, Circle):
            return self.radius == other.radius

    def __lt__(self, other):
        """
        Compare the radius of this circle with another circle (less than).

        :param other: The other Circle object to compare with.
        :return: True if this circle's radius is less than the other circle's radius.
        """
        if isinstance(other, Circle):
            return self.radius < other.radius

    def __le__(self, other):
        """
        Compare the radius of this circle with another circle (less than or equal).

        :param other: The other Circle object to compare with.
        :return: True if this circle's radius is less than or equal to the other circle's radius.
        """
        if isinstance(other, Circle):
            return self.radius <= other.radius

    def __gt(self, other):
        """
        Compare the radius of this circle with another circle (greater than).

        :param other: The other Circle object to compare with.
        :return: True if this circle's radius is greater than the other circle's radius.
        """
        if isinstance(other, Circle):
            return self.radius > other.radius

    def __ge(self, other):
        """
        Compare the radius of this circle with another circle (greater than or equal).

        :param other: The other Circle object to compare with.
        :return: True if this circle's radius is greater than or equal to the other circle's radius.
        """
        if isinstance(other, Circle):
            return self.radius >= other.radius

    def __repr__(self):
        """
        Get a string representation of the Circle object.
        """
        return f"Circle(radius={self.radius}, x={self.x}, y={self.y})"

    def __str__(self):
        """
        Get a user-friendly string representation of the Circle object.
        """
        return f"Circle with radius {self.radius} at ({self.x}, {self.y})"

    def is_unit_circle(self):
        """
        Check if this circle is a unit circle (radius equal to 1).

        :return: True if the circle is a unit circle, otherwise False.
        """
        return self.radius == 1
    
    def draw_geometry(self):
        drawing_circle = plt.Circle((self.x, self.y), self.radius, color="blue", fill=False, linewidth=3)
        ax = plt.gca()
        ax.set(xlim=(-15, 15), ylim=(-15, 15))
        ax.add_patch(drawing_circle)
        ax.plot(point_x, point_y, "ko")
        ax.set_aspect("equal", "box")
        plt.show()

# objects
circle_1 = Circle(5, 0, 0)
circle_2 = Circle(6, 0, 0)

"""
# tests manual
print(circle_1)
print(f"Area: {circle_1.area}")
print(f"Circumference: {circle_1.circumference}")
print(circle_1.center_point())
print(circle_1.check_position(point_x, point_y))
print(f"circle_1 == circle_2: {circle_1 == circle_2}")
circle_1.move_geometry(5, 5)
print(circle_1.center_point())
circle_1.draw_geometry()
print(circle_1.check_position(point_x, point_y))
"""
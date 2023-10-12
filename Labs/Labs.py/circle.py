import matplotlib.pyplot as plt
import math
from random_points import random_point


"""This code defines a class called "Circle" to represent circles. 
It includes methods for calculating the circle's area, circumference, 
checking if a point is inside the circle, and comparing circles. Additionally,
 it allows for moving the circle's position and visualizing it using Matplotlib."""

# Define a class named Circle.
class Circle:
    # Initialize the Circle with radius, x, and y coordinates.
    def __init__(self, radius, x, y):
        # Set the radius, ensuring it's a valid length.
        self.radius = self.validate_length(radius)
        # Set the x and y coordinates, ensuring they are valid real numbers.
        self.x, self.y = self.validate_real_numbers(x, y)

    # Define a property to calculate and return the area of the circle.
    @property
    def area(self):
        return math.pi * self.radius ** 2

    # Define a property to calculate and return the circumference of the circle.
    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    # Define a method to get the center point of the circle.
    def center_point(self):
        return self.x, self.y

    # Define a method to move the circle's position to new coordinates.
    def move_geometry(self, move_x, move_y):
        self.x, self.y = self.validate_real_numbers(move_x, move_y)

    # Define a method to check if a given point is inside the circle.
    def check_position(self, point_x, point_y):
        return (point_x - self.x) ** 2 + (point_y - self.y) ** 2 <= self.radius ** 2

    # Define a method to check if the circle is a unit circle (radius equal to 1).
    def is_unit_circle(self):
        return self.radius == 1

    # Define a static method to validate that a value (length) is greater than 0 and raise an exception if not.
    @staticmethod
    def validate_length(value):
        if value <= 0:
            raise ValueError(f"Length must be > 0, not {value}")
        return value

    # Define a static method to validate that both x and y are either integers or floats, and raise an exception if not.
    @staticmethod
    def validate_real_numbers(x, y):
        for val in (x, y):
            if not isinstance(val, (int, float)):
                raise TypeError(f"Coordinates must be int or float, not {type(val)}")
        return x, y

    # Define a method to compare if two circles are equal (have the same radius).
    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius

    # Define a method to compare if one circle is less than another (based on radius).
    def __lt__(self, other):
        return isinstance(other, Circle) and self.radius < other.radius

    # Define a method to compare if one circle is less than or equal to another (based on radius).
    def __le__(self, other):
        return isinstance(other, Circle) and self.radius <= other.radius

    # Define a method to compare if one circle is greater than another (based on radius).
    def __gt(self, other):
        return isinstance(other, Circle) and self.radius > other.radius

    # Define a method to compare if one circle is greater than or equal to another (based on radius).
    def __ge__(self, other):
        return isinstance(other, Circle) and self.radius >= other.radius

    # Define a method to generate a string representation of the Circle object.
    def __repr__(self):
        return f"Circle (radius={self.radius}, x={self.x}, y={self.y})"

    # Define a method to draw a 2D representation of the circle using Matplotlib.
    def draw_geometry(self):
        drawing_circle = plt.Circle((self.x, self.y), self.radius, color="blue", fill=False, linewidth=3)
        ax = plt.gca()
        ax.set(xlim=(-15, 15), ylim=(-15, 15))
        ax.add_patch(drawing_circle)
        ax.plot(point_x, point_y, "ko")
        ax.set_aspect("equal", "box")
        plt.show()

# Generate random point coordinates.
point_x, point_y, _ = random_point()

# Create two Circle objects with different radii and positions.
circle_1 = Circle(5, 1, 1)
circle_2 = Circle(6, 2, 3)

# Testing and printing results.
print(circle_1)
print(f"Area: {circle_1.area}")
print(f"Circumference: {circle_1.circumference}")
print(f"Center Point: {circle_1.center_point()}")
print(f"Point Inside Circle: {circle_1.check_position(point_x, point_y)}")
print(f"Is Unit Circle: {circle_1.is_unit_circle()}")
print(f"circle_1 == circle_2: {circle_1 == circle_2}")

# Move the first circle to a new position.
circle_1.move_geometry(5, 5)
print(circle_1)
print(f"Point Inside Circle (after move): {circle_1.check_position(point_x, point_y)}")

# Draw a 2D representation of the circle.
circle_1.draw_geometry()


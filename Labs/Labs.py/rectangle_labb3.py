import matplotlib.pyplot as plt
import math
from random_points import random_point

class Rectangle:
    def __init__(self, side1, side2, x, y):
        """Initialize a rectangle with given side lengths and position."""
        self.side1 = self.validate_length(side1)
        self.side2 = self.validate_length(side2)
        self.x, self.y = self.validate_real_numbers(x, y)

    @property
    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.side1 * self.side2

    @property
    def circumference(self):
        """Calculate and return the circumference of the rectangle."""
        return 2 * (self.side1 + self.side2)

    def center_point(self):
        """Calculate and return the coordinates of the center point of the rectangle."""
        return self.x + (self.side1 / 2), self.y + (self.side2 / 2)

    def move_geometry(self, move_x, move_y):
        """Move the rectangle to a new position defined by the given coordinates."""
        self.x, self.y = self.validate_real_numbers(move_x, move_y)

    def check_position(self, point_x, point_y):
        """Check if a given point with coordinates (point_x, point_y) is inside the rectangle."""
        return self.x <= point_x <= (self.x + self.side1) and self.y <= point_y <= (self.y + self.side2)

    @staticmethod
    def validate_length(value):
        """Validate that a value (length) is greater than zero and raise an exception if not."""
        if value <= 0:
            raise ValueError(f"Length must be > 0, not {value}")
        return value

    @staticmethod
    def validate_real_numbers(x, y):
        """Validate that both x and y are either integers or floats, and raise an exception if not."""
        for val in (x, y):
            if not isinstance(val, (int, float)):
                raise TypeError(f"Numbers must be int or float, not {type(val)}")
        return x, y

    def is_square(self):
        """Check if the rectangle is a square (both sides are equal)."""
        return self.side1 == self.side2

    def __eq__(self, other):
        """Check if another object is also a Rectangle and has the same side lengths."""
        return isinstance(other, Rectangle) and (self.side1 == other.side1 and self.side2 == other.side2)

    def __repr__(self):
        """Return a string representation of the Rectangle object."""
        return f"Rectangle (side1={self.side1}, side2={self.side2}, x={self.x}, y={self.y})"

    def draw_2d_geometry(self):
        """Draw a 2D representation of the rectangle using Matplotlib."""
        drawing_rectangle = plt.Rectangle((self.x, self.y), self.side1, self.side2, color="red", fill=False, linewidth=2)
        ax = plt.gca()
        ax.set(xlim=(-15, 15), ylim=(-15, 15))
        ax.add_patch(drawing_rectangle)
        ax.plot(point_x, point_y, "ko")
        ax.set_aspect("equal", "box")
        plt.show()

# Random point coordinates
point_x, point_y, _ = random_point()

# Create rectangle objects
rectangle_1 = Rectangle(5, 10, 1, 1)
rectangle_2 = Rectangle(3, 3, 2, 3)
rectangle_3 = Rectangle(4, 1, -2, -3)

# Testing and printing results
print(rectangle_1)
print(f"Area: {rectangle_1.area}")
print(f"Circumference: {rectangle_1.circumference}")
print(f"Center Point: {rectangle_1.center_point()}")
print(f"Point Inside Rectangle: {rectangle_1.check_position(point_x, point_y)}")
print(f"Is Square: {rectangle_1.is_square()}")
print(f"rectangle_1 == rectangle_2: {rectangle_1 == rectangle_2}")
rectangle_1.move_geometry(-5, -5)
print(rectangle_1)
print(f"Point Inside Rectangle (after move): {rectangle_1.check_position(point_x, point_y)}")
rectangle_1.draw_2d_geometry()
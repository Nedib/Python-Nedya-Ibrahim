import math
from randompoint import random_point
from Geometry import Geometry  
import matplotlib.pyplot as plt

# Generate random coordinates
point_x, point_y, point_z = random_point()  # Override with your own coordinates

class Rectangle(Geometry):
    """
    Represents a rectangle in 2D space.

    Attributes:
    width (float): Width of the rectangle.
    height (float): Height of the rectangle.
    x (float): X-coordinate of the rectangle's position.
    y (float): Y-coordinate of the rectangle's position.
    """

    def __init__(self, width, height, x, y):
        """
        Initialize a Rectangle instance.

        Args:
        width (float): Width of the rectangle.
        height (float): Height of the rectangle.
        x (float): X-coordinate of the rectangle's position.
        y (float): Y-coordinate of the rectangle's position.
        """
        super().__init__(x, y)
        self.width = width
        self.height = height
        Rectangle.validate_length(width, height)
        Rectangle.validate_real_numbers(width, height)

    @property
    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
        float: The area of the rectangle.
        """
        return self.width * self.height

    @property
    def circumference(self):
        """
        Calculate the circumference of the rectangle.

        Returns:
        float: The circumference of the rectangle.
        """
        return 2 * (self.width + self.height)

    def center_point(self):
        """
        Calculate the center point of the rectangle.

        Returns:
        tuple: A tuple containing the (x, y) coordinates of the rectangle's center point.
        """
        return (self.x, self.y)

    def move_geometry(self, new_x, new_y):
        """
        Move the rectangle to new coordinates.

        Args:
        new_x (float): New X-coordinate.
        new_y (float): New Y-coordinate.
        """
        self.x = new_x
        self.y = new_y

    def is_inside(self, x, y):
        """
        Check if a given point is inside the rectangle.

        Args:
        x (float): X-coordinate of the point.
        y (float): Y-coordinate of the point.

        Returns:
        bool: True if the point is inside the rectangle, False otherwise.
        """
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height

    @staticmethod
    def validate_length(*values):
        """
        Validate that given values are greater than 0.

        Args:
        *values: Variable-length list of values to validate.

        Raises:
        ValueError: If any value is less than or equal to 0.
        """
        for val in values:
            if val <= 0:
                raise ValueError(f"Length must be > 0, not {val}")
            Rectangle.validate_real_numbers(val)

    def __eq__(self, other):
        """
        Compare if this rectangle is equal to another rectangle based on dimensions.

        Args:
        other (Rectangle): Another Rectangle object to compare.

        Returns:
        bool: True if the rectangles have equal dimensions, considering width and height.
        """
        if isinstance(other, Rectangle):
            return (self.width == other.width and self.height == other.height) or \
                   (self.width == other.height and self.height == other.width)

    def __repr__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        str: A string representation of the rectangle's attributes.
        """
        return f"Rectangle(width={self.width}, height={self.height}, x={self.x}, y={self.y})"

    def draw_geometry(self):
        """
        Draw the rectangle.

        Visualizes the rectangle using Matplotlib and adds it to the current plot.
        """
        drawing_rectangle = plt.Rectangle((self.x, self.y), self.width, self.height, color="red", fill=False, linewidth=2)
        ax = plt.gca()
        ax.set(xlim=(-15, 15), ylim=(-15, 15))
        ax.add_patch(drawing_rectangle)
        ax.plot(point_x, point_y, "ko")
        ax.set_aspect("equal", "box")
        plt.show()
"""
# tests manual
rectangle_1 = Rectangle(5, 10, 0, 0)
rectangle_2 = Rectangle(3, 3, 0, 0)
rectangle_3 = Rectangle(1, 4, 0, 0)
print(rectangle_1)
print(rectangle_1.area)
print(rectangle_1.circumference)
print(rectangle_1.center_point())
print(rectangle_1.is_inside(point_x, point_y))
print(f"rectangle_1 == rectangle_2: {rectangle_1 == rectangle_2}")
rectangle_1.move_geometry(-5, -5)
print(rectangle_1.center_point())
rectangle_1.draw_geometry()
"""
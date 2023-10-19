import math
import random as random
from randompoint import random_point
import matplotlib.pyplot as plt

point_x, point_y, point_z = random_point()  

class Geometry:
    """
    Represents a geometric shape in 2D space.

    Attributes:
    x (float): X-coordinate of the shape's position.
    y (float): Y-coordinate of the shape's position.
    """

    def __init__(self, x, y):
        """
        Initialize a Geometry instance.

        Args:
        x (float): X-coordinate of the shape's position.
        y (float): Y-coordinate of the shape's position.
        """
        self.x = float(x)
        self.y = float(y)

    def area(self):
        """
        Calculate the area of the geometric shape.

        This method should be implemented by subclasses.

        Raises:
        NotImplementedError: This method should be implemented in subclasses.

        Returns:
        float: The area of the shape.
        """
        pass

    def circumference(self):
        """
        Calculate the circumference of the geometric shape.

        This method should be implemented by subclasses.

        Raises:
        NotImplementedError: This method should be implemented in subclasses.

        Returns:
        float: The circumference of the shape.
        """
        pass

    def center_point(self):
        """
        Calculate the center point (centroid) of the geometric shape.

        Returns:
        tuple: A tuple containing the (x, y) coordinates of the shape's center point.
        """
        return self.x, self.y

    def move_geometry(self, new_x, new_y):
        """
        Move the geometric shape to new coordinates.

        Args:
        new_x (float): New X-coordinate.
        new_y (float): New Y-coordinate.
        """
        self.x = new_x
        self.y = new_y

    def check_position(self, point_x, point_y):
        """
        Check if a given point is within the geometric shape.

        Args:
        point_x (float): X-coordinate of the point.
        point_y (float): Y-coordinate of the point.

        Returns:
        bool: True if the point is inside the shape, False otherwise.
        """
        pass

    def is_inside(self, x, y):
        """
        Check if a given point is inside the geometric shape.

        Args:
        x (float): X-coordinate of the point.
        y (float): Y-coordinate of the point.

        Returns:
        bool: True if the point is inside the shape, False otherwise.
        """
        pass

    @staticmethod
    def validate_length(value):
        """
        Validate that a given value is greater than 0.

        Args:
        value (float): The value to validate.

        Raises:
        ValueError: If the value is less than or equal to 0.
        """
        if value <= 0:
            raise ValueError(f"Length must be > 0, not {value}")

    @staticmethod
    def validate_real_numbers(*values):
        """
        Validate that given values are integers or floats.

        Args:
        *values: Variable-length list of values to validate.

        Raises:
        TypeError: If any value is not an int or float.
        """
        for val in values:
            if not isinstance(val, (int, float)):
                raise TypeError(f"Values must be int or float, not {type(val)}")

    def __eq__(self, other):
        """
        Compare if this shape is equal to another shape based on area.

        Args:
        other (Geometry): Another Geometry object to compare.

        Returns:
        bool: True if the shapes have equal areas, False otherwise.
        """
        if isinstance(other, Geometry):
            return self.area() == other.area()

    def __repr__(self):
        """
        Return a string representation of the shape.

        Returns:
        str: A string representation of the shape's attributes.
        """
        return f"Geometry(x={self.x}, y={self.y})"

    def draw_geometry(self):
        """
        Draw the geometric shape, which should be implemented in subclasses.

        This method should be implemented by subclasses to visualize the shape.
        """
        pass
import math
import randompoint as random  # Make sure you import randompoint from the correct location
import matplotlib.pyplot as plt

# Generate random coordinates
point_x, point_y, point_z = random.random_point()  # Override with your own coordinates

class Rectangle:
    """
    A class for creating rectangular shapes with specified width and height. The 'x' and 'y' attributes represent the
    coordinates of the top-left corner of the rectangle. This class provides methods to calculate the area, circumference,
    and center point of the rectangle. It also allows for repositioning the rectangle and checking if a given point lies
    within its boundaries. Static methods 'validate_length' and 'validate_real_numbers' ensure input validity. The class
    supports comparison based on the equality of dimensions (width and height) and includes a method to plot the rectangle
    and a random point on a 2D graph.
    """
    def __init__(self, width, height, x, y):
        """
        Create a 2D rectangular shape with specified width and height, positioned at the top-left corner (x, y).
        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
            x (float): The x-coordinate of the top-left corner of the rectangle.
            y (float): The y-coordinate of the top-left corner of the rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Rectangle.validate_length(width, height)
        Rectangle.validate_real_numbers(width, height, x, y)

    def area(self):
        """
        Calculate and return the area of the rectangle.
        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def circumference(self):
        """
        Calculate and return the circumference of the rectangle.
        Returns:
            float: The circumference of the rectangle.
        """
        return 2 * (self.width + self.height)

    def center_point(self):
        """
        Return the coordinates of the center point of the rectangle.
        Returns:
            Tuple[float, float]: The coordinates of the center point (x, y).
        """
        return self.x + self.width / 2, self.y + self.height / 2

    def move_geometry(self, new_x, new_y):
        """
        Reposition the rectangle to new coordinates.
        Args:
            new_x (float): The new x-coordinate of the top-left corner of the rectangle.
            new_y (float): The new y-coordinate of the top-left corner of the rectangle.
        """
        self.x = new_x
        self.y = new_y

    def check_position(self, point_x, point_y):
        """
        Check if a given point is inside the rectangle.
        Args:
            point_x (float): The x-coordinate of the point.
            point_y (float): The y-coordinate of the point.
        Returns:
            bool: True if the point is inside the rectangle, False otherwise.
        """
        x1, x2 = self.x, self.x + self.width
        y1, y2 = self.y, self.y + self.height
        return x1 <= point_x <= x2 and y1 <= point_y <= y2

    @staticmethod
    def validate_length(*values):
        """
        Validate the length values to ensure they are positive.
        Args:
            *values: Variable-length arguments for values to validate.
        Raises:
            ValueError: If any of the values is non-positive.
        """
        for val in values:
            if val <= 0:
                raise ValueError(f"Length must be > 0, not {val}")
        Rectangle.validate_real_numbers(*values)

    @staticmethod
    def validate_real_numbers(*values):
        """
        Validate that the values are real numbers (int or float).
        Args:
            *values: Variable-length arguments for values to validate.
        Raises:
            TypeError: If any of the values is not an int or float.
        """
        for val in values:
            if not isinstance(val, (int, float)):
                raise TypeError(f"Values must be int or float, not {type(val)}")

    def __eq__(self, other):
        """
        Check if another object is an equivalent rectangle, considering both width and height.
        Args:
            other (object): The object to compare with.
        Returns:
            bool: True if the other object is an equivalent rectangle, False otherwise.
        """
        if isinstance(other, Rectangle):
            return (self.width == other.width and self.height == other.height) or \
                   (self.width == other.height and self.height == other.width)

    def __repr__(self):
        """
        Return a string representation of the rectangle.
        Returns:
            str: String representation of the rectangle.
        """
        return f"Rectangle(width={self.width}, height={self.height}, x={self.x}, y={self.y})"

    def draw_geometry(self):
        """
        Draw the rectangle and a point on a 2D graph using Matplotlib.
        """
        drawing_rectangle = plt.Rectangle((self.x, self.y), self.width, self.height, color="red", fill=False, linewidth=2)
        ax = plt.gca()
        ax.set(xlim=(-15, 15), ylim=(-15, 15))
        ax.add_patch(drawing_rectangle)
        ax.plot(point_x, point_y, "ko")
        ax.set_aspect("equal", "box")
        plt.show()

# Example usage
rectangle_1 = Rectangle(5, 10, 0, 0)
rectangle_2 = Rectangle(3, 3, 0, 0)
rectangle_3 = Rectangle(1, 4, 0, 0)
print(rectangle_1)
print(rectangle_1.area())
print(rectangle_1.circumference())
print(rectangle_1.center_point())
print(rectangle_1.check_position(point_x, point_y))
print(f"rectangle_1 == rectangle_2: {rectangle_1 == rectangle_2}")
rectangle_1.move_geometry(-5, -5)
print(rectangle_1.center_point())
rectangle_1.draw_geometry()
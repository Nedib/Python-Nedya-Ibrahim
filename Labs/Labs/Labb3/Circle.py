import math
import randompoint as random  # Make sure you import randompoint from the correct location
import matplotlib.pyplot as plt

# Generate random coordinates
point_x, point_y, point_z = random.random_point()  # Override with your own coordinates

class Circle:
    """
    A class for creating geometric circles with specified radius. The 'x' and 'y' attributes represent the coordinates
    of the circle's center. This class provides methods to calculate the area and circumference of the circle, determine
    the center point, move the circle to new coordinates, and check if a given point lies within its boundaries. Static
    methods 'validate_length' and 'validate_real_numbers' ensure input validity. The class supports comparison based on
    the equality of radii and includes a method to plot the circle and a random point on a 2D graph.
    """
    def __init__(self, radius, x, y):
        """
        Create a 2D circle object with a specified radius and center coordinates.
        Args:
            radius (float): The radius of the circle.
            x (float): The x-coordinate of the circle's center.
            y (float): The y-coordinate of the circle's center.
        """
        self.radius = radius
        self.x = x
        self.y = y
        Circle.validate_length(radius)
        Circle.validate_real_numbers(radius, x, y)

    def area(self):
        """
        Calculate and return the area of the circle.
        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def circumference(self):
        """
        Calculate and return the circumference of the circle.
        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.radius

    def center_point(self):
        """
        Return the coordinates of the circle's center.
        Returns:
            Tuple[float, float]: The coordinates of the center (x, y).
        """
        return self.x, self.y

    def move_geometry(self, new_x, new_y):
        """
        Move the circle to new coordinates.
        Args:
            new_x (float): The new x-coordinate of the circle's center.
            new_y (float): The new y-coordinate of the circle's center.
        """
        self.x = new_x
        self.y = new_y

    def check_position(self, point_x, point_y):
        """
        Check if a given point is inside the circle.
        Args:
            point_x (float): The x-coordinate of the point.
            point_y (float): The y-coordinate of the point.
        Returns:
            bool: True if the point is inside the circle, False otherwise.
        """
        d2 = (point_x - self.x) ** 2 + (point_y - self.y) ** 2
        return d2 <= self.radius ** 2

    @staticmethod
    def validate_length(value):
        """
        Validate the length (radius) of the circle.
        Args:
            value (float): The value to validate.
        Raises:
            ValueError: If the length is non-positive.
        """
        if value <= 0:
            raise ValueError(f"Length must be > 0, not {value}")
        Circle.validate_real_numbers(value)

    @staticmethod
    def validate_real_numbers(*values):
        """
        Validate if the values are real numbers (int or float).
        Args:
            *values: Variable-length arguments to validate.
        Raises:
            TypeError: If any value is not an int or a float.
        """
        for val in values:
            if not isinstance(val, (int, float)):
                raise TypeError(f"Values must be int or float, not {type(val)}")

    def __eq__(self, other):
        """
        Check if another object is a circle with the same radius.
        Args:
            other (object): The object to compare with.
        Returns:
            bool: True if the other object is a matching circle, False otherwise.
        """
        if isinstance(other, Circle):
            return self.radius == other.radius

    def __repr__(self):
        """
        Return a string representation of the circle.
        Returns:
            str: String representation of the circle.
        """
        return f"Circle(radius={self.radius}, x={self.x}, y={self.y})"

    def draw_geometry(self):
        """
        Draw the circle and a point on a 2D graph using Matplotlib.
        """
        drawing_circle = plt.Circle((self.x, self.y), self.radius, color="blue", fill=False, linewidth=3)
        ax = plt.gca()
        ax.set(xlim=(-15, 15), ylim=(-15, 15))
        ax.add_patch(drawing_circle)
        ax.plot(point_x, point_y, "ko")
        ax.set_aspect("equal", "box")
        plt.show()

# Example usage
circle_1 = Circle(5, 0, 0)
circle_2 = Circle(6, 0, 0)
print(circle_1)
print(circle_1.area())
print(circle_1.circumference())
print(circle_1.center_point())
print(circle_1.check_position(point_x, point_y))
print(f"circle_1 == circle_2: {circle_1 == circle_2}")
circle_1.move_geometry(5, 5)
print(circle_1.center_point())
circle_1.draw_geometry()
print(circle_1.check_position(point_x, point_y))
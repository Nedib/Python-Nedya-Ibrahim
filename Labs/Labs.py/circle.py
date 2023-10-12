import matplotlib.pyplot as plt
import math
from random_points import random_point

class Circle:
    def __init__(self, radius, x, y):
        self.radius = self.validate_length(radius)
        self.x, self.y = self.validate_real_numbers(x, y)

    @property
    def area(self):
        return math.pi * self.radius ** 2
    
    @property
    def circumference(self):
        return 2 * math.pi * self.radius
    
    def center_point(self):
        return self.x, self.y

    def move_geometry(self, move_x, move_y):
        self.x, self.y = self.validate_real_numbers(move_x, move_y)

    def check_position(self, point_x, point_y):
        return (point_x - self.x) ** 2 + (point_y - self.y) ** 2 <= self.radius ** 2

    
    def is_unit_circle(self):
        return self.radius == 1  

    @staticmethod
    def validate_length(value):
        if value <= 0:
            raise ValueError(f"Length must be > 0, not {value}")
        return value

    @staticmethod
    def validate_real_numbers(x, y):
        for val in (x, y):
            if not isinstance(val, (int, float)):
                raise TypeError(f"Coordinates must be int or float, not {type(val)}")
        return x, y

    
    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius

   
    def __lt__(self, other):
        return isinstance(other, Circle) and self.radius < other.radius

   
    def __le__(self, other):
        return isinstance(other, Circle) and self.radius <= other.radius

    
    def __gt__(self, other):
        return isinstance(other, Circle) and self.radius > other.radius

    
    def __ge__(self, other):
        return isinstance(other, Circle) and self.radius >= other.radius

    def __repr__(self):
        return f"Circle (radius={self.radius}, x={self.x}, y={self.y})"

    def draw_geometry(self):
        drawing_circle = plt.Circle((self.x, self.y), self.radius, color="blue", fill=False, linewidth=3)
        ax = plt.gca()
        ax.set(xlim=(-15, 15), ylim=(-15, 15))
        ax.add_patch(drawing_circle)
        ax.plot(point_x, point_y, "ko")
        ax.set_aspect("equal", "box")
        plt.show()


point_x, point_y, _ = random_point()


circle_1 = Circle(5, 1, 1)
circle_2 = Circle(6, 2, 3)


circle_1 = Circle(5, 1, 1)
print(f"Area: {circle_1.area}")
print(f"Circumference: {circle_1.circumference}")
print(f"Center Point: {circle_1.center_point()}")
print(f"Point Inside Circle: {circle_1.check_position(point_x, point_y)}")
print(f"Is Unit Circle: {circle_1.is_unit_circle()}")
print(f"circle_1 == circle_2: {circle_1 == circle_2}")
circle_1.move_geometry(5, 5)
print(circle_1)
print(f"Point Inside Circle (after move): {circle_1.check_position(point_x, point_y)}")
circle_1.draw_geometry()


import matplotlib.pyplot as plt
import math
import numpy as np

from circle.labb3 import Circle

from random_points import random_point

class Sphere(Circle):
    def __init__(self, radius, x, y, z):
        super().__init__(radius, x, y)
        self.z = z

    @property
    def sphere_area(self):
        return 4 * math.pi * self.radius ** 2

    @property
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    def move_3d_geometry(self, move_x, move_y, move_z):
        self.x, self.y, self.z = self.validate_real_numbers(move_x, move_y, move_z)

    def is_unit_sphere(self):
        return self.radius == 1

    def check_position(self, point_x, point_y, point_z):
        d_squared = (point_x - self.x) ** 2 + (point_y - self.y) ** 2 + (point_z - self.z) ** 2
        return d_squared <= self.radius ** 2

    def __eq__(self, other):
        return isinstance(other, Sphere) and self.radius == other.radius

    def __repr__(self):
        return f"Sphere (radius={self.radius}, x={self.x}, y={self.y}, z={self.z})"


# Slumpmässiga punktkoordinater
point_x, point_y, point_z = random_point()

# Skapa sphere-objekt
sphere_1 = Sphere(4, 1, 1, 1)
sphere_2 = Sphere(5, 2, 1, 2)

# Testning
print(sphere_1)
print(f"Area: {sphere_1.sphere_area}")
print(f"Volume: {sphere_1.volume}")
print(f"Point Inside Sphere: {sphere_1.check_position(point_x, point_y, point_z)}")
print(f"Is Unit Sphere: {sphere_1.is_unit_sphere()}")
print(f"sphere_1 == sphere_2: {sphere_1 == sphere_2}")
sphere_1.move_3d_geometry(5, 5, 5)
print(sphere_1)
print(f"Point Inside Sphere (after move): {sphere_1.check_position(point_x, point_y, point_z)}")
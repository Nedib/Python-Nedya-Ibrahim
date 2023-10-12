import matplotlib.pyplot as plt
import math
import numpy as np
from rectangle_labb3 import Rectangle
from random_points import random_point

"""The code defines a Cube class that inherits from Rectangle, allowing the creation 
and manipulation of 3D cube objects. It includes methods for calculating properties,
 checking point positions, and visualizing the cubes. Test cases are provided for
   demonstration."""

class Cube(Rectangle): # Initialize a cube with given side length and 3D position.
    def __init__(self, side_length, x, y, z):
        super().__init__(side_length, side_length, x, y)
        self.z = z

    def cube_area(self):
        return 6 * self.side1 ** 2

    def circumradius(self):
        return self.side1 * math.sqrt(3) / 2

    def center_point(self):
        cube_center_x = self.x + (self.side1 / 2)
        cube_center_y = self.y + (self.side1 / 2)
        cube_center_z = self.z + (self.side1 / 2)
        return cube_center_x, cube_center_y, cube_center_z

    def volume(self):
        return self.side1 ** 3

    def move_3d_geometry(self, move_x, move_y, move_z):
        self.x, self.y, self.z = move_x, move_y, move_z

    def check_position(self, point_x, point_y, point_z):
        x1, x2 = self.x, self.x + self.side1
        y1, y2 = self.y, self.y + self.side1
        z1, z2 = self.z, self.z + self.side1

        return x1 <= point_x <= x2 and y1 <= point_y <= y2 and z1 <= point_z <= z2

    def __eq__(self, other):
        return isinstance(other, Cube) and self.side1 == other.side1

    def __repr__(self):
        return f"Cube (side_length={self.side1}, x={self.x}, y={self.y}, z={self.z})"

    def draw_3d_geometry(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        a = self.side1
        x, y, z = self.get_cube()

        dx, dy, dz = self.x, self.y, self.z

        ax.plot_surface(x * a + dx, y * a + dy, z * a + dz, alpha=0.25)
        plt.plot(point_x, point_y, point_z, "ko")

        ax.set_xlim(-15, 15)
        ax.set_ylim(-15, 15)
        ax.set_zlim(-15, 15)
        plt.show()

    @staticmethod
    def get_cube():
        phi = np.arange(1, 10, 2) * np.pi / 4
        phi2, theta = np.meshgrid(phi, phi)
        x_cube = np.cos(phi2) * np.sin(theta)
        y_cube = np.sin(phi2) * np.sin(theta)
        z_cube = np.cos(theta) / np.sqrt(2)
        return x_cube, y_cube, z_cube

# Slumpmässiga punktkoordinater
point_x, point_y, point_z = random_point()

# Skapa cube-objekt
cube_1 = Cube(5, 0, 0, 0)
cube_2 = Cube(4, 1, 1, 1)

# Testning
print(cube_1)
print(f"Area: {cube_1.cube_area()}")
print(f"Circumradius: {cube_1.circumradius()}")
print(f"Center Point: {cube_1.center_point()}")
print(f"Point Inside Cube: {cube_1.check_position(point_x, point_y, point_z)}")
print(f"cube_1 == cube_2: {cube_1 == cube_2}")
cube_1.move_3d_geometry(6, 6, 6)
print(cube_1)
print(f"Point Inside Cube (after move): {cube_1.check_position(point_x, point_y, point_z)}")
cube_1.draw_3d_geometry()
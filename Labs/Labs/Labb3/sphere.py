import matplotlib.pyplot as plt
import numpy as np
import math
from circle import Circle

class Sphere(Circle):
    """
    A class representing a 3D sphere.

    Attributes:
        radius (float): The radius of the sphere.
        x (float): The x-coordinate of the sphere's center.
        y (float): The y-coordinate of the sphere's center.
        z (float): The z-coordinate of the sphere's center.
    """

    def __init__(self, radius, x, y, z):
        """
        Initialize a new Sphere instance.

        Args:
            radius (float): The radius of the sphere.
            x (float): The x-coordinate of the sphere's center.
            y (float): The y-coordinate of the sphere's center.
            z (float): The z-coordinate of the sphere's center.
        """
        super().__init__(radius, x, y)
        self.z = z

    def area(self):
        """
        Calculate the surface area of the sphere.

        Returns:
            float: The surface area of the sphere.
        """
        return 4 * math.pi * self.radius ** 2

    def circumference(self):
        """
        Calculate the circumference of the sphere.

        Returns:
            float: The circumference of the sphere.
        """
        return 2 * math.pi * self.radius

    def center_point(self):
        """
        Get the center point of the sphere.

        Returns:
            tuple: A tuple containing the x, y, and z coordinates of the center point.
        """
        return self.x, self.y, self.z

    def move_geometry(self, new_x, new_y, new_z):
        """
        Move the sphere to a new center point.

        Args:
            new_x (float): The new x-coordinate for the center.
            new_y (float): The new y-coordinate for the center.
            new_z (float): The new z-coordinate for the center.
        """
        self.x, self.y, self.z = new_x, new_y, new_z

    def check_position(self, point_x, point_y, point_z):
        """
        Check if a point is inside the sphere.

        Args:
            point_x (float): The x-coordinate of the point to check.
            point_y (float): The y-coordinate of the point to check.
            point_z (float): The z-coordinate of the point to check.

        Returns:
            bool: True if the point is inside the sphere, False otherwise.
        """
        d_squared = (point_x - self.x) ** 2 + (point_y - self.y) ** 2 + (point_z - self.z) ** 2
        return d_squared <= self.radius ** 2

    def is_unit_sphere(self):
        """
        Check if the sphere is a unit sphere (radius = 1).

        Returns:
            bool: True if the sphere is a unit sphere, False otherwise.
        """
        return self.radius == 1

    def __eq__(self, other):
        """
        Compare if two spheres are equal.

        Args:
            other (Sphere): The other sphere to compare to.

        Returns:
            bool: True if the spheres have the same radius, False otherwise.
        """
        return isinstance(other, Sphere) and self.radius == other.radius

    def __repr__(self):
        """
        Get a string representation of the sphere.

        Returns:
            str: A string representation of the sphere.
        """
        return f"Sphere (radius={self.radius}, x={self.x}, y={self.y}, z={self.z})"

    def draw_3d_geometry(self):
        """
        Draw a 3D representation of the sphere.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        u = np.linspace(0, 2 * math.pi, 100)
        v = np.linspace(0, math.pi, 100)
        x = self.x + self.radius * np.outer(np.cos(u), np.sin(v))
        y = self.y + self.radius * np.outer(np.sin(u), np.sin(v))
        z = self.z + self.radius * np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_surface(x, y, z, color='b', alpha=0.5)

        ax.set_xlim(self.x - self.radius, self.x + self.radius)
        ax.set_ylim(self.y - self.radius, self.y + self.radius)
        ax.set_zlim(self.z - self.radius, self.z + self.radius)
        ax.scatter([point_x], [point_y], [point_z], color='r', s=100,)
        ax.legend()
        plt.show()

point_x, point_y, point_z = np.random.rand() * 8, np.random.rand() * 8, np.random.rand() * 8

sphere_1 = Sphere(4, 1, 1, 1)
sphere_2 = Sphere(5, 2, 1, 2)

"""
print(sphere_1)
print(f"Area: {sphere_1.area}")
print(f"Circumference: {sphere_1.circumference}")
print(f"Center Point: {sphere_1.center_point()}")
print(f"Point Inside Sphere: {sphere_1.check_position(point_x, point_y, point_z)}")
print(f"Is Unit Sphere: {sphere_1.is_unit_sphere()}")
print(f"sphere_1 == sphere_2: {sphere_1 == sphere_2}")
sphere_1.move_geometry(5, 5, 5)
print(sphere_1)
print(f"Point Inside Sphere (after move): {sphere_1.check_position(point_x, point_y, point_z)}")
sphere_1.draw_3d_geometry()
"""
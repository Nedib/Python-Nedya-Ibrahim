import matplotlib.pyplot as plt
import numpy as np
import math
from Circle import Circle  # Ensure the correct import path for the Circle class
from randompoint import random_point  # Make sure to import random_point from the correct location

class Sphere(Circle):
    """
    A class for creating 3D spheres that inherit properties and methods from the Circle class.
    This class allows you to calculate the surface area, volume, and perform various 3D operations on spheres.
    It also supports visualization of spheres in 3D space.
    """
    def __init__(self, radius, x, y, z):
        """
        Create a 3D sphere with the specified radius and position.
        Args:
            radius (float): The radius of the sphere.
            x (float): The x-coordinate of the center of the sphere.
            y (float): The y-coordinate of the center of the sphere.
            z (float): The z-coordinate of the center of the sphere.
        """
        super().__init__(radius, x, y)  # Call the constructor of the Circle class
        self.z = z  # Set the z-coordinate

    @property
    def sphere_area(self):
        """
        Calculate and return the surface area of the sphere.
        Returns:
            float: The surface area of the sphere.
        """
        return 4 * math.pi * self.radius ** 2

    @property
    def volume(self):
        """
        Calculate and return the volume of the sphere.
        Returns:
            float: The volume of the sphere.
        """
        return (4/3) * math.pi * self.radius ** 3

    def move_3d_geometry(self, move_x, move_y, move_z):
        """
        Move the sphere to a new 3D position defined by the given coordinates.
        Args:
            move_x (float): The new x-coordinate of the center of the sphere.
            move_y (float): The new y-coordinate of the center of the sphere.
            move_z (float): The new z-coordinate of the center of the sphere.
        """
        self.x, self.y, self.z = move_x, move_y, move_z  # Update the coordinates

    def is_unit_sphere(self):
        """
        Check if the sphere is a unit sphere (radius is 1).
        Returns:
            bool: True if it's a unit sphere, False otherwise.
        """
        return self.radius == 1

    def check_position(self, point_x, point_y, point_z):
        """
        Check if a given 3D point is inside the sphere.
        Args:
            point_x (float): The x-coordinate of the point.
            point_y (float): The y-coordinate of the point.
            point_z (float): The z-coordinate of the point.
        Returns:
            bool: True if the point is inside the sphere, False otherwise.
        """
        d_squared = (point_x - self.x) ** 2 + (point_y - self.y) ** 2 + (point_z - self.z) ** 2
        return d_squared <= self.radius ** 2

    def __eq__(self, other):
        """
        Check if another object is an equivalent sphere, considering the radius.
        Args:
            other (object): The object to compare with.
        Returns:
            bool: True if the other object is an equivalent sphere, False otherwise.
        """
        return isinstance(other, Sphere) and self.radius == other.radius

    def __repr__(self):
        """
        Return a string representation of the sphere.
        Returns:
            str: String representation of the sphere.
        """
        return f"Sphere (radius={self.radius}, x={self.x}, y={self.y}, z={self.z}"

    def draw_3d_geometry(self):
        """
        Draw the sphere in a 3D plot using Matplotlib.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')  # Create a 3D plot

        u = np.linspace(0, 2 * math.pi, 100)
        v = np.linspace(0, math.pi, 100)
        x = self.x + self.radius * np.outer(np.cos(u), np.sin(v))
        y = self.y + self.radius * np.outer(np.sin(u), np.sin(v))
        z = self.z + self.radius * np.outer(np.ones(np.size(u)), np.cos(v))

        ax.plot_surface(x, y, z, color='b', alpha=0.5)  # Draw 3D geometry

        ax.set_xlim(self.x - self.radius, self.x + self.radius)
        ax.set_ylim(self.y - self.radius, self.y + self.radius)
        ax.set_zlim(self.z - self.radius, self.z + self.radius)
        plt.plot([point_x], [point_y], [point_z], "ro")
        plt.show()  # Display 3D geometry

point_x, point_y, point_z = np.random.rand() * 8, np.random.rand() * 8, np.random.rand() * 8  # Generate random point coordinates

# Create sphere objects
sphere_1 = Sphere(4, 1, 1, 1)
sphere_2 = Sphere(5, 2, 1, 2)

# Test and print results
print(sphere_1)
print(f"Area: {sphere_1.sphere_area}")
print(f"Volume: {sphere_1.volume}")
print(f"Point Inside Sphere: {sphere_1.check_position(point_x, point_y, point_z)}")
print(f"Is Unit Sphere: {sphere_1.is_unit_sphere()}")
print(f"sphere_1 == sphere_2: {sphere_1 == sphere_2}")
sphere_1.move_3d_geometry(5, 5, 5)
print(sphere_1)
print(f"Point Inside Sphere (after move): {sphere_1.check_position(point_x, point_y, point_z)}")
sphere_1.draw_3d_geometry()
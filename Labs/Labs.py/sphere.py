import matplotlib.pyplot as plt  # Import the library for 3D visualization
import math  # Import the mathematical library
import numpy as np  # Import the numerical library
from circle import Circle  # Import the circle class
from random_points import random_point  # Import the random point function

"""The code defines a Sphere class that inherits from Circle, enabling 3D spherical geometry operations.
 It calculates properties, validates positions, and visualizes spheres in a 3D plot.
   Test cases demonstrate its functionalities."""

class Sphere(Circle):
    def __init__(self, radius, x, y, z):
        super().__init__(radius, x, y)  # Use the circle's constructor
        self.z = z  # Set the z-coordinate

    @property
    def sphere_area(self):
        return 4 * math.pi * self.radius ** 2  # Calculate and return the surface area

    @property
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3  # Calculate and return the volume

    def move_3d_geometry(self, move_x, move_y, move_z):
        self.x, self.y = self.validate_real_numbers(move_x, move_y)  # Move the x and y coordinates
        self.z = self.validate_length(move_z)  # Update the z-coordinate

    def is_unit_sphere(self):
        return self.radius == 1  # Check if it's a unit sphere

    def check_position(self, point_x, point_y, point_z):
        d_squared = (point_x - self.x) ** 2 + (point_y - self.y) ** 2 + (point_z - self.z) ** 2
        return d_squared <= self.radius ** 2  # Check if a point is inside

    def __eq__(self, other):
        return isinstance(other, Sphere) and self.radius == other.radius  # Compare spheres

    def __repr__(self):
        return f"Sphere (radius={self.radius}, x={self.x}, y={self.y}, z={self.z})"  # String representation

    def draw_3d_geometry(self):
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

        plt.show()  # Show 3D geometry

point_x, point_y, point_z = random_point()  # Generate random point coordinates

sphere_1 = Sphere(4, 1, 1, 1)  # Create a sphere with radius 4 and position
sphere_2 = Sphere(5, 2, 1, 2)  # Create another sphere with radius 5 and position

print(sphere_1)  # Print the text representation of the sphere
print(f"Area: {sphere_1.sphere_area}")  # Print the surface area
print(f"Volume: {sphere_1.volume}")  # Print the volume
print(f"Point Inside Sphere: {sphere_1.check_position(point_x, point_y, point_z)}")  # Check if a point is inside
print(f"Is Unit Sphere: {sphere_1.is_unit_sphere()}")  # Check if it's a unit sphere
print(f"sphere_1 == sphere_2: {sphere_1 == sphere_2}")  # Compare spheres
sphere_1.move_3d_geometry(5, 5, 5)  # Move the sphere's position
print(sphere_1)  # Print the new position
print(f"Point Inside Sphere (after move): {sphere_1.check_position(point_x, point_y, point_z)}")  # Check if a point is inside
sphere_1.draw_3d_geometry()  # Draw 3D geometry





from rectangle import Rectangle
from randompoint import random_point
import matplotlib.pyplot as plt
import numpy as np

def random_point():
    """
    Generate random 3D coordinates.

    Returns:
    tuple: A tuple containing three random coordinates (x, y, z).
    """
    return 8 * np.random.rand(), 8 * np.random.rand(), 8 * np.random.rand()

# Generate random coordinates
point_x, point_y, point_z = random_point()

class Cube(Rectangle):
    """
    Represents a 3D cube, a subclass of Rectangle.
    """

    def __init__(self, width, height, x, y, z):
        """
        Initialize a Cube instance.

        Args:
        width (float): Width of the cube.
        height (float): Height of the cube.
        x (float): X-coordinate of the cube's position.
        y (float): Y-coordinate of the cube's position.
        z (float): Z-coordinate of the cube's position.
        """
        super().__init__(width, height, x, y)
        self.z = z

    def area(self):
        """
        Calculate the surface area of the cube.

        Returns:
        float: The surface area of the cube.
        """
        return 6 * self.width * self.height

    def circumference(self):
        """
        Calculate the total edge length of the cube.

        Returns:
        float: The total edge length of the cube.
        """
        return 4 * (self.width + self.height + self.height)

    def center_point(self):
        """
        Calculate the center point (centroid) of the cube.

        Returns:
        tuple: A tuple containing the (x, y, z) coordinates of the cube's center point.
        """
        cube_center_x = self.x + (self.width / 2)
        cube_center_y = self.y + (self.height / 2)
        cube_center_z = self.z + (self.height / 2)
        return cube_center_x, cube_center_y, cube_center_z

    def move_geometry(self, new_x, new_y):
        """
        Move the cube's position to new coordinates.

        Args:
        new_x (float): New X-coordinate.
        new_y (float): New Y-coordinate.
        """
        self.x = new_x
        self.y = new_y

    def check_position(self, point_x, point_y, point_z):
        """
        Check if a given point is within the cube.

        Args:
        point_x (float): X-coordinate of the point.
        point_y (float): Y-coordinate of the point.
        point_z (float): Z-coordinate of the point.

        Returns:
        bool: True if the point is inside the cube, False otherwise.
        """
        x1, x2 = self.x, self.x + self.width
        y1, y2 = self.y, self.y + self.height
        z1, z2 = self.z, self.z + self.height
        return x1 <= point_x <= x2 and y1 <= point_y <= y2 and z1 <= point_z <= z2

    def __eq__(self, other):
        """
        Compare if this cube is equal to another cube.

        Args:
        other (Cube): Another Cube object to compare.

        Returns:
        bool: True if the cubes are equal, False otherwise.
        """
        return isinstance(other, Cube) and (self.width == other.width and self.height == other.height)

    def __repr__(self):
        """
        Return a string representation of the cube.

        Returns:
        str: A string representation of the cube's attributes.
        """
        return f"Cube (width={self.width}, height={self.height}, x={self.x}, y={self.y}, z={self.z})"

    def draw_geometry(self):
        """
        Draw the cube's geometry using 3D plotting.

        This method uses Matplotlib to create a 3D plot of the cube and a point in space.
        """
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        a = self.width
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
        """
        Generate cube coordinates for 3D plotting.

        Returns:
        tuple: Three arrays (x, y, z) for cube coordinates in 3D space.
        """
        phi = np.arange(1, 10, 2) * np.pi / 4
        phi2, theta = np.meshgrid(phi, phi)
        x_cube = np.cos(phi2) * np.sin(theta)
        y_cube = np.sin(phi2) * np.sin(theta)
        z_cube = np.cos(theta) / np.sqrt(2)
        return x_cube, y_cube, z_cube

# objects
cube_1 = Cube(5, 5, 0, 0, 0)
cube_2 = Cube(4, 4, 1, 1, 1)

"""
## tests manual
print(cube_1)
print(f"Area: {cube_1.area()}")
print(f"circumference: {cube_1.circumference()}")
print(f"Center Point: {cube_1.center_point()}")
print(f"Point Inside Cube: {cube_1.check_position(point_x, point_y, point_z)}")
print(f"cube_1 == cube_2: {cube_1 == cube_2}")
cube_1.move_geometry(6, 6)
print(cube_1)
print(f"Point Inside Cube (after move): {cube_1.check_position(point_x, point_y, point_z)}")
cube_1.draw_geometry()
"""
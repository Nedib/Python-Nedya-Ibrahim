import matplotlib.pyplot as plt
import numpy as np
import math
from rectangle import Rectangle  

def random_point():
    """
    Simulate random 3D point coordinates within a specified range.
    Returns:
        Tuple[float, float, float]: Random point coordinates (x, y, z).
    """
    return 8 * np.random.rand(), 8 * np.random.rand(), 8 * np.random.rand()

# Random point coordinates
point_x, point_y, point_z = random_point()

class Cube(Rectangle):
    def __init__(self, width, height, x, y, z):
        """
        Create a 3D cube object.
        Args:
            width (float): The width of the cube.
            height (float): The height of the cube.
            x (float): The x-coordinate of the cube.
            y (float): The y-coordinate of the cube.
            z (float): The z-coordinate of the cube.
        """
        super().__init__(width, height, x, y)  # Call the constructor of the Rectangle class
        self.z = z

    def cube_area(self):
        """
        Calculate and return the surface area of the cube.
        Returns:
            float: The surface area of the cube.
        """
        return 6 * self.width * self.height

    def circumradius(self):
        """
        Calculate and return the circumradius of the cube.
        Returns:
            float: The circumradius of the cube.
        """
        return self.width * math.sqrt(3) / 2

    def center_point(self):
        """
        Calculate and return the coordinates of the cube's center point in 3D.
        Returns:
            Tuple[float, float, float]: Coordinates of the center point (x, y, z).
        """
        cube_center_x = self.x + (self.width / 2)
        cube_center_y = self.y + (self.height / 2)
        cube_center_z = self.z + (self.height / 2)
        return cube_center_x, cube_center_y, cube_center_z

    def volume(self):
        """
        Calculate and return the volume of the cube.
        Returns:
            float: The volume of the cube.
        """
        return self.width * self.height * self.height

    def move_3d_geometry(self, move_x, move_y, move_z):
        """
        Move the cube to a new 3D position specified by the given coordinates.
        Args:
            move_x (float): The new x-coordinate of the cube.
            move_y (float): The new y-coordinate of the cube.
            move_z (float): The new z-coordinate of the cube.
        """
        self.x, self.y, self.z = move_x, move_y, move_z

    def check_position(self, point_x, point_y, point_z):
        """
        Check if a given 3D point with coordinates (point_x, point_y, point_z) is inside the cube.
        Args:
            point_x (float): x-coordinate of the point to check.
            point_y (float): y-coordinate of the point to check.
            point_z (float): z-coordinate of the point to check.
        Returns:
            bool: True if the point is inside the cube, False otherwise.
        """
        x1, x2 = self.x, self.x + self.width
        y1, y2 = self.y, self.y + self.height
        z1, z2 = self.z, self.z + self.height
        return x1 <= point_x <= x2 and y1 <= point_y <= y2 and z1 <= point_z <= z2

    def __eq__(self, other):
        """
        Check if another object is a cube and has the same width and height.
        Args:
            other (object): The object to compare with.
        Returns:
            bool: True if the other object is a matching cube, False otherwise.
        """
        return isinstance(other, Cube) and (self.width == other.width and self.height == other.height)

    def __repr__(self):
        """
        Return a string representation of the cube.
        Returns:
            str: String representation of the cube.
        """
        return f"Cube (width={self.width}, height={self.height}, x={self.x}, y={self.y}, z={self.z})"

    def draw_3d_geometry(self):
        """
        Draw a 3D representation of the cube using Matplotlib.
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
        Generate cube coordinates for 3D visualization.
        Returns:
            Tuple[np.array, np.array, np.array]: Cube coordinates (x, y, z).
        """
        phi = np.arange(1, 10, 2) * np.pi / 4
        phi2, theta = np.meshgrid(phi, phi)
        x_cube = np.cos(phi2) * np.sin(theta)
        y_cube = np.sin(phi2) * np.sin(theta)
        z_cube = np.cos(theta) / np.sqrt(2)
        return x_cube, y_cube, z_cube

# Random point coordinates
point_x, point_y, point_z = random_point()

# Create cube objects
cube_1 = Cube(5, 5, 0, 0, 0)
cube_2 = Cube(4, 4, 1, 1, 1)

# Test and print results
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
import matplotlib.pyplot as plt  
import math  
import numpy as np  
from rectangle_labb3 import Rectangle  
from random_points import random_point  

"""The code defines a Cube class that inherits from Rectangle, allowing the creation 
and manipulation of 3D cube objects. It includes methods for calculating properties,
 checking point positions, and visualizing the cubes. Test cases are provided for demonstration."""

class Cube(Rectangle): # Initialize a cube with given side length and 3D position.
    def __init__(self, side_length, x, y, z):
        super().__init__(side_length, side_length, x, y)  # Call the constructor of the Rectangle class
        self.z = z  # Set the z-coordinate for the cube

    def cube_area(self): #Calculate and return the surface area of the cube.
        return 6 * self.side1 ** 2

    def circumradius(self): #Calculate and return the circumradius of the cube.
        return self.side1 * math.sqrt(3) / 2

    def center_point(self): #Calculate and return the coordinates of the center point of the cube.
        cube_center_x = self.x + (self.side1 / 2)
        cube_center_y = self.y + (self.side1 / 2)
        cube_center_z = self.z + (self.side1 / 2)
        return cube_center_x, cube_center_y, cube_center_z

    def volume(self): #Calculate and return the volume of the cube.
        return self.side1 ** 3
    
    """Move the cube to a new 3D position defined by the given coordinates."""
    def move_3d_geometry(self, move_x, move_y, move_z):
        self.x, self.y, self.z = move_x, move_y, move_z

    def check_position(self, point_x, point_y, point_z):#Check if a given 3D point with coordinates (point_x, point_y, point_z) is inside the cube.
        x1, x2 = self.x, self.x + self.side1
        y1, y2 = self.y, self.y + self.side1
        z1, z2 = self.z, self.z + self.side1
        return x1 <= point_x <= x2 and y1 <= point_y <= y2 and z1 <= point_z <= z2

    def __eq__(self, other): #Check if another object is also a Cube and has the same side length.
        return isinstance(other, Cube) and self.side1 == other.side1

    def __repr__(self): #Return a string representation of the Cube object.
        return f"Cube (side_length={self.side1}, x={self.x}, y={self.y}, z={self.z})"

    def draw_3d_geometry(self):#Draw a 3D representation of the cube using Matplotlib.
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
    def get_cube(): #Generate cube coordinates for 3D visualization.
        phi = np.arange(1, 10, 2) * np.pi / 4
        phi2, theta = np.meshgrid(phi, phi)
        x_cube = np.cos(phi2) * np.sin(theta)
        y_cube = np.sin(phi2) * np.sin(theta)
        z_cube = np.cos(theta) / np.sqrt(2)
        return x_cube, y_cube, z_cube

# Random point coordinates
point_x, point_y, point_z = random_point()

# Create cube objects
cube_1 = Cube(5, 0, 0, 0)
cube_2 = Cube(4, 1, 1, 1)

# Testing and printing results
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

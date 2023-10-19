import random

def random_point():
    """Generate random x, y, and z coordinates for a point within the range of -10 to 10."""


    point_x = random.randint(-10, 10)
    point_y = random.randint(-10, 10)
    point_z = random.randint(-10, 10)
    
    return point_x, point_y, point_z


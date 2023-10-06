#import matplotlib.pyplot as plt
#from random points import random points

class Rectangel:
    def __init__(self, side1, side2, x, y):
        self.side1 = self.validate_length(side1)   
        self.side2 = self.validate_length(side2)
        self.x,self.y = self.validate_real_number(x,y) 

    def area(self):
        return self.side1 * self.side2
    
    def circumference(self):
        return 2 * (self.side1 + self.side2)
    
    def center_point(self):
        return self.x + (self.side1/2), self.y + (self.side2/2)
    
    def move_geometry(self)

        
        
    
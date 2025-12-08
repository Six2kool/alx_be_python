# polymorphism_demo.py
import math   # we need this for math.pi

# The "boss" class – every shape must obey this rule
class Shape:
    def area(self):
        raise NotImplementedError("Hey! Every shape has to write its own area() method!")


# First kid: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    # This REPLACES the boss's area() method → this is called "overriding"
    def area(self):
        return self.length * self.width


# Second kid: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    # Its own special way of calculating area
    def area(self):
        return math.pi * self.radius * self.radius
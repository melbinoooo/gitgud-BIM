# Inheritance:
# A class can also inherit the attributes of an existing class.

# The to be inherited class will be called: 
# Base Class or (Parent Class).

# The one who will inherit the property of a class is called:
# Derived Class or (Child Class).


# Derived Class inherits the features of its parent class.
# and it can also add new features into it.

#----------------------------------------#



# Part 1: Creating the base class for polygon:

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = []
        for i in range(no_of_sides):
            self.sides.append(0)
            
    def input_sides(self):
        for i in range(self.n):
            self.sides[i] = float(input("Enter side"+str(i+1)+" :"))


# Inheriting Triangle from Polygon Class
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
    
    def find_area(self):
        a, b, c = self.sides
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is: ', area)

t = Triangle()
t.input_sides()
t.find_area()
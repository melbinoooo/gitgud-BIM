# Python Constructors:
# A Class functions that begins with two underscores
# are called "special functions"
# as they gets automatically called whenever a new object/instances is initiated.

# e.g.
# "__init__"



#----------------------------------------#
# Part 1: Sample Constructor

from turtle import distance


class SampleClass:
    def __init__(self, z1 = 0, z2 = 2):
        self.a = z1
        self.b = z2

sample_object1 = SampleClass()
print(sample_object1.a) # Output: 0
print(sample_object1.b) # Output: 2

sample_object2 = SampleClass(10, 20)
print(sample_object2.a) # Output: 10
print(sample_object2.b) # Output: 20




#----------------------------------------#
# Part 2: Sample [Find Distance from Origin]

class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def distance(self):
        """Find distance from origin"""
        return (self.x**2 + self.y**2) ** 0.5

samplePoint1 = Point(6,8)
distance = samplePoint1.distance()

print(distance)
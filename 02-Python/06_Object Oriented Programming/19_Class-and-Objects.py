# Class and Objects


# What is a 'Class'
# Class = Type
# e.g. 
# Type = Human

# What is an 'Object'
# Object = Instance of Type/Class
# e.g.
# OBJECT = Human No. 1


# Another analogy:
# Class = Blood Type
# Instances = Blood A / Blood AB / Blood O

#----------------------------------------#
# Part 1: Creating a Basic Class
# Using "Class" before the Capitalized-name.
# We can also embed an attirbute and a function within a Class. 

class SampleClass:
    a = 10 # Attributes
    def samplefunc(self): # Function
        return 'Hello'



#----------------------------------------#
# Part 2: Creating an Object
# In order to access that attributes and the function of a class.
# We need to make an instance out of it, by creating an object.


sample_object1 = SampleClass()
print(sample_object1.a) # This prints out the 'a' attribute of the class. // # 10
print(sample_object1.samplefunc()) # This prints out the samplefunc(self) of the class // # Hello



#----------------------------------------#
# Part 3: Overriding the attribute of the Class

sample_object2 = SampleClass()

sample_object2.a = 35
print(sample_object2.a) # This overrides the 'a' value of the SampleClass and prints out "35".



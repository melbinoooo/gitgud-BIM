# What are modules? 
# Modules refers to a container which contain statement and definitions in Python.
# Modules are used to break down large chunk of codes into small ones.



#----------------------------------------#
# Part 1: Creating and Importing Modules
# We are using SampleModule.py



#----------------------------------------#
# Part 2: Importing SampleModule.py
# And now we can use the functions inside SampleModule by using it as an extention.


import SampleModule as SM

result = SM.add(2,4)
print(result) # Output: 6



#----------------------------------------#
# Part 3: Importing Built in Modules in Python like Math

import math

x = 5
y = 10


# Get SquareRoot
get_square_root = math.sqrt(x)
print(get_square_root) # Output: 2.23606797749

# Get Log of Y
get_log = math.log(y)
print("Log of Y: ", get_log) # Output: Log of Y:  2.302585092994046


#----------------------------------------#
# Part 4: Importing Selected Functions only.
# Using "From" then "Import"

from math import pi, e
# We Import only the pi & e

pi_times_x = x * pi
print(pi_times_x) # Output: 15.707963267948966

# Print 'e' value from math.
print("Print e-value: ",e) # Output: Print e-value:  2.718281828459045



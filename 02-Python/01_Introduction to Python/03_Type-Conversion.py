# Part 1
# Type Conversion is the process of converting one value to another type of value.
# Integer samples= 1, 3, 0, -10, -25,
# Float samples = 0.5, 2.5, -10.5


# Converting a float number into an integer by using the command "int()"
# Example: Using the literal float value of 123.456 into integer. 

# Input: 123.456
# Covert to Integer
# Output: 123
print(int(123.456))


# Another example using variables.

sample_float_number = 50.23
convert_to_integer = int(sample_float_number)
print(convert_to_integer)
# Input: sample_float_number // which is 50.23
# Convert to integer using the variable "convert_to_integer", which has a value of int()
# Output: 50




#----------------------------------------#
# Part 2
# Converting a string to a Float.
# A string is a character that is inside a (" ") or (' ')


sample_string = '8765.40000'
string_to_float = float(sample_string)
print(string_to_float)

# Input: '8765.4000' String.
# Output: 8765.4

# However, we cannot convert a string into integer, for the reason that python recognize a pure numerical value as an integer already and it doesn't recognize a number that is treated as a string-value.


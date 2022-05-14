# Using Variables and Literal Values for Mathematical and Logical Computations.
# Known Samples of an Operators are: (+, -, /, =)
# Multiplication, Addition, Subtraction, Division, etc.

#----------------------------------------#
# Part 1: Adding Variables

x = 10
y = 20
sum = x + y
print(sum)

# Input: "x" for 10, and "y" for 20.
# sum variable: consists of variable "x" and "y".
# Output: Sum of variable "x" and "y" is 30, using the operator "+"


# Note: This will also behave for other operators (multiple, divide, subtract, etc).



#----------------------------------------#
# Part 2
# You can also use Operators to combine string values.

sample_animal = "cat"
sample_color = "white"
animal_color = sample_color + " " +sample_animal

print(animal_color)

# If we did not use an operator, the program will produce a list, like this:
# Output: animal_color = {white, cat}

# However, if we did use an operator to combine the two strings, it'll look like this:
# Output: white cat 



#----------------------------------------#
# Part 3
# We can use the operators to multiple strings as well.
# For example: We needed to repeat the word "tweet" 3 times.

sample_word = "tweet"
b = sample_word*3
print(b)

# Output: tweettweettweet


#----------------------------------------#
# Part 4
# PEMDAS
# The Operators will follow the rule of PEMDAS (Parenthesis, Exponent, Multiplication, Division, Addition, Subtraction).
# Here as an example, we will get a different output just because of how the operators has been laid out differently.


# Sample 1
f = 30
g = 20
h = 10
print(f - g * h)
# Output: -170
# In this case the Multiplication has been done first then following with the subtraction.


# Sample 2
print((f - g)* h)
# Output: 100
# In this case, the operator within the parenthesis has been done first, then multiplication.









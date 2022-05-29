# What is a Function?
# A function is what performs a specific tasks.
# e.g. 'print()'


# Input -> 'Function' -> Output



#----------------------------------------#
# Part 1: Defining a Function

# def function_name(parameters):
#    statement(s)

# Keyword 'def' defining the function
# function_name is the Function
# (parameters) are used to passed value to the function


#----------------------------------------#
# Part 2: Creating a simple Function


def user_name(name): #Function Header
    print("Hello", name) #Statement
    
user_name('Paul') #Function Call


#----------------------------------------#
# Part 3: Adding Numbers using a defined Function

def add_numbers(n1, n2): #Defined Function
    sum = n1+n2 #Statement
    print("Sum =", sum)

num1 = 10 #Variable to use for Function Call
num2 = 20 #Variable to use for Function Call

add_numbers(num1, num2) #Function Call

# Output: Sum = 30


#----------------------------------------#
# Part 4: Subtracting Numbers using a defined Function and a Return statement

def subtract_numbers(n1, n2):
    difference = n2-n1
    return difference #return statement is used to exit the function.

result = subtract_numbers(20, 10)
print("Difference =", result)

# Output: Difference = 10


#----------------------------------------#
# Part 5: User-defined Functions vs Built-in Functions

# Built-in Function samples:
# print()
# range()
# input()

# User-defined Functions are:
# created using the "def"

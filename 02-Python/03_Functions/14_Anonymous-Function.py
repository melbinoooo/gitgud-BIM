# Anonymous Functions

# We can define a function without defining its name.

# The syntax for the Lambda function is
# function = lambda expression


#----------------------------------------#

# Part 1: Lambda Function

square = lambda n: n*n # This is a lambda function

result = square(3) # This is a Function Call

print(result) # This is the print statement
#Output : 9





# The above program is equivalent to:




def n_square(x): # This is a defined function
    return x*x # This is a return statement

result = n_square(3) # This is a Function Call
print(result) # This is the print statement
#Output : 9
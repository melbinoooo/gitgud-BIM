# Boolean = True / False
# Boolean Expressions are basically a set of programs that can make a decisions.
# For instance: if the statement is true; do this | if the statement is false; do that.

# Samples of Boolean Operators
# < Less than
# > Greater than
# == Equal to
# != Not equal to
# >= Greathan or Equal to
# <= Less than or Equal to


#----------------------------------------#
# Part 1: Simple Boolean Expression

print(20 > 30)
# Output: False // because 20 is not greater than 30. 


print(20 != 30)
# Output: True // because 20 is not equal to 30.


#----------------------------------------#
# Part 2: Logical Boolean Operators

# Samples of Logical Boolean Operators are:
# "and" gives back an output of "True" if both are operands are "True", and "False" if it's not.
# "or" gives back an output of "True" if either one of the operands are "True".
# "not" gives back an output of "True" if both operands are "False".

# Straight Forward Sample
print(True and True) # Output: True, because both are true.
print(True or False) # Output: True, because one is true.
print(not False) #Output: True, because the statement is not false.


# Numerical Example
print(6>3 and 6>2) #Output: True, because 6 is both greater than 3 and 2.
print(6>3 or 6>8) #Output: True, because one is true than the other.

a = 5
print(not (a == 5)) 
# Output: False, because a is equal to 5 but it receives a "not" boolean.
# Easier to read it as: The statement is saying that a is not equal to 5, the statement is wrong, that is why it proceeded to output a "False".

# (not (a == 5)) // remember PEMDAS
# (not (true)) // False



print(not (a != 5))
# Output: True, because a is indeed equal to 5, but it receives a "not" boolean.
# Easeir to read it as: The statement within the parenthesis (a != 5) is false, therefore it proceeded to the next statement which is "not" False, therefore it's true.

# (not (a != 5)) // remember PEMDAS
# (not (false)) // True




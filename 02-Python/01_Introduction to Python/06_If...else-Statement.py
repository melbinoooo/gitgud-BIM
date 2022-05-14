# The if statement is a command executed based on the boolean expression.
# The if statement will be executed if the boolean expression is True.
# The if statement will be skipped if the boolean expression is False.



#----------------------------------------#
# Part 1: Simple If Statement

sample_number = 5

if sample_number > 3:
    print("Print this if it is true.")
print("This command is required to end the if statement.")
# The command [print("Print this if it is true.")] has been executed because 5 > 3 is True.


if sample_number > 6:
    print("Print this if it is true.")
print("This command is required to end the if statement.")
# The command [print("Print this if it is true.")] has not been executed or been skipped because 5 > 6 is False.


# The command [print("This command is requried to end the if statement.")], is requried to be added as a fall back for the if statement if the statement appears to be false and in order to end the command.


#----------------------------------------#
# Part 2: If...else Statement
# The if..else statement basically means:
# If the statement is true, do this, however if it appears to be false, do this instead.

if sample_number > 6:
    print("Print this if it is true.")
    
else:
    print("Print this if it is false.")

# The else's statement is the output because 5 is not greater than 6, therefore execute the else statement instead.


#----------------------------------------#
# Part 3: Adding the else...if Statement a.k.a "elif"
# The if else statement gaves us an option to choose between two outputs.
# The else if statement gave us more than 2 choices of outputs.


if sample_number > 6:
    print("Print this if it is true.")
elif sample_number == 5:
    print("sample_number is equal to 5")
else:
    print("Print this if it is false.")

# This simply read as:
# if 5 is greater than 6, print this// but it happened to be false since 5 is not greater than 6.
# else... if 5 is equal to 5, print this// the statement is true, therefore it proceed to execute the command inside the elif statement.
# The else statement has been skipped since the elif statement has appear to be "true" first.



#----------------------------------------#
# Part 4: Nested If...else statement
# This just means that there is an If...statement inside the If...statement


sample_input_number = float(input("Enter a number: "))

if sample_input_number >= 5:
    if sample_input_number == 5:
        print("Your input is equal to 5")
    else:
        print("This is not equal to 5")
else:
    print("This is not greater than 5")
    
# This reads as: 
# if the sample_input_number is greater than or equal to 5, execute the internal if else statement.
# if the sample_input_number is not greater than or not equal to 5, execute this exiting else statement.

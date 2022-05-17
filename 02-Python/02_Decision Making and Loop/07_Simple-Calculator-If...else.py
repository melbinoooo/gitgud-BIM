# Creating a simple calculator using inputs and if...else statements.



#----------------------------------------#
# Part 1: Creating Variables

print("What are you calculating?")

operator = input("Enter either: addition, subtraction, multiplication, division: ")


n1 = float(input("Enter First Number: "))
n2 = float(input("Enter Second Number: "))

addition = n1+n2
subtraction = n1-n2
multiplication = n1*n2
division = n1/n2

if operator == 'addition':
    print(n1, '+', n2, '=', addition)
elif operator == 'subtraction':
    print(n1, '-', n2, '=', subtraction)
elif operator == 'multiplcation':
    print(n1, '*', n2, '=', multiplication)
elif operator == 'division':
    print(n1, '/', n2, '=', division)
else:
    print("invalid operator")
    

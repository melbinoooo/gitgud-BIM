# While loop
# is a block of code
# which continuously run
# until the boolean statement is true



#----------------------------------------#
# Part 1: Simple loop (While)

n = 5
i = 1

while i <= n:
    i = i+1 
    print("Looping...")


# Explanation:
# The operator is i = i+1
# If variable i is less than or equal to variable n in every iterations or code runs.
# It will keep printing ("Looping") until variable i became greater than variable n.



#----------------------------------------#
# Part 2: Infinite Loop

# The while loop will keep running if the boolean always returns true; and never false.

# nn = 5
# ii = 1

# while ii <= nn:
#     i = i-1
#     print("Infinite Loop")
    
    

#----------------------------------------#
# Part 3: Getting the Sum of all natural numbers until n = 10

nnn = 10

sum = 0
iii = 1

while iii <= nnn:
    sum = sum+iii 
    iii = iii+1    
    print("The sum is:", sum)


# Explanation:
# 1 = 0 + 1
# 2 = 1 + 1 // iii = 2

# 3 = 1 + 2
# 3 = 2 + 1 // iii = 3

# 6 = 3 + 3
# 4 = 3 + 1 // iii = 4

# 10 = 6 + 4
# 5 = 4 + 1 // iii = 5

# 15 = 10 + 5
# 6 = 5 + 1 // iii = 6

# 21 = 15 + 6
# 7 = 6 + 1 // iii = 7

# 28 = 21 + 7
# 8 = 7 + 1 // iii = 8

# 36 = 28 + 8
# 9 = 8 + 1 // iii = 9

# 45 = 36 + 9
# 10 = 9 + 1 // iii = 10 

# 55 = 45 + 10
# iii = 10 + 1 // iii = 11 # the operation is less than or 'equal to' 10.
# #iterations stops here 
# because variable iii is greater than and not equal to nnn '10'


#----------------------------------------#
# Part 4: While loop with Else statement
# Basically, after the number of loops based on boolean 'true', it will run the else statement:


counter = 0
while counter < 3:
    print("counter: ", counter)
    counter = counter + 1
    
else:
    print("counting done")
    


#----------------------------------------#
# Part 5: Exercise: Multiplication Table for 13.

num = 13
mult = 1

while mult <= 10:
    print(num, 'x', mult, '=', num*mult)
    mult = mult+1
else:
    print('Multiplication Table of 13 is done!')

# What is iterate?
# - A sequence of code being repeated continuously until a targeted result is achieved.

# Sample of "Sequences":
# Strings = sequence of characters e.g. sample_string = "a,b,c,1,2"
# Lists = sequence of items encapsulated in a square brackets e.g. sample_list = ["testing", 22, 45, sample_string]
# Range = sequence of a predicted range of numbers e.g. = sample_range = range(1, 45)



#----------------------------------------#
# Part 1: Understanding the syntax of (for_loop)

# for val in sequence: // "val" is a variable that takes the value of each item inside the sequence of each iterations.
# statement(s)


# Sample
courses = ['English', 'Science', 'Math']

for val in courses:
    print(val)

# Output: 
# English
# Science
# Math


#----------------------------------------#
# Part 2: Sum from 1 to 101

numbers = range(1,101)
sum = 0 # This acts as a placeholder for 'sum'

for i in numbers:
    sum += i #every iteration of sum it adds the appropriate turn of range.
print('Sum =', sum)


# Output: 5050
# Explanation:
# every iteration of sum it adds the appropriate turn of the range.
# for the iteration for this 'for loop' looks like this:

# sum += 1 #first iteration of the range (1,101)
# this equation write down as: sum = 0 + 1

# sum += 3 #second iteration of the range (2,101)
# this equation write down as: sum = 1 + 2

# sum += 6 #third iteration of the range (3,101)
# this equation write down as: sum = 3 + 3

# sum += 10 #fourth iteration of the range (4,101)
# this equation write down as: sum = 6 + 4

# sum += 15 #fourth iteration of the range (5,101)
# this equation write down as: sum = 10 + 5

# this runs until it reaches the range (101,101)
# which equation write down as: sum = 4950 + 100




#----------------------------------------#
# Part 3: Viewing for loop in Multiplacation

n = 22

for i in range(1,11):
    print(n, 'x', i, '=', n*i)


# Output
# 22 x 1 = 22
# 22 x 2 = 44
# 22 x 3 = 66
# 22 x 4 = 88
# 22 x 5 = 110
# 22 x 6 = 132
# 22 x 7 = 154
# 22 x 8 = 176
# 22 x 9 = 198
# 22 x 10 = 220



#----------------------------------------#
# Part 4: for loop with else statement
# Basically means when the iteration "target end" ends, it'll run the else statement

sample_list = ['for loop 1', 'for loop 2']

for list in sample_list:
    print(list)

else:
    print('for loop 3 / this list ends')

# Output: 
# for loop 1 #1st iteration of list 
# for loop 2 #2nd/last iteration of list
# for loop 3 / this list ends # else statement
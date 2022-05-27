# What is Break and Continue?

# Loop continuously run until it reach the target or it arrives at 'False'.
# The break statement terminates the loop where it is being written.

# The break statement is always used with the "if statement"
# e.g.


# for list in sample_list:
# ...
# if test_break_expression:
#   break
# ...


#----------------------------------------#
# Part 1: Using 'break' in range sequence

for i in range(1,11):
    if i == 5:
        break
    print(i)

# Output:
# 1
# 2
# 3
# 4 # the range stops here, because the next sequence is '5', because as it the break statement is 'i == 5'



#----------------------------------------#
# Part 2: Using 'continue' in range sequence

for i in range(1,11):
    if i == 5:
        continue
    print(i)

# Output:
# 1
# 2
# 3
# 4
# continue # the number 5 is voided because, the if statement is 'i == 5'
# the 'continue' will literally continue the sequence until it reaches the target or met 'False"
# 6
# 7
# 8
# 9
# 10

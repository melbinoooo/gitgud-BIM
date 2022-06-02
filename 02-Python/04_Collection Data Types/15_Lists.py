# Lists are created when putting values inside a parenthesis. "[ 1, 2, 3 ]"



#----------------------------------------#
# Part 1: Creating a simple Lists.

sample_number_list = [1, 2, 3, 4]
sample_string_list = ["AE", "AI", "AO", "AU"]

sample_variable1 = "sample variable 1"
sample_variable2 = "sample variable 2"

sample_variable_list = [sample_variable1, sample_variable2]
print(sample_variable_list)

# Output: "sample variable 1", "sample variable 2"


#----------------------------------------#
# Part 2: Indexing the list

sample_to_index_list = [1, 2, 3, 4, 5]
print(sample_to_index_list[0]) # This prints 1
print(sample_to_index_list[2]) # This prints 3
print(sample_to_index_list[4]) # This prints 5

# Indexing starts with "0"



#----------------------------------------#
# Part 3: Negative indexing
# Negative indexing has the same concept as the normal one, instead it starts at the end.
# Negative indexing also starts with -1, rather than "0"

#sample_to_index_list = [1, 2, 3, 4, 5]
print(sample_to_index_list[-1]) # This prints 5
print(sample_to_index_list[-3]) # This prints 3
print(sample_to_index_list[-5]) # This prints 1



#----------------------------------------#
# Part 4: Slicing a Lists
# Slicing is basically stateing where to start after the stated index count.

sample_to_slice = [10, 20, 30, 40, 50]
print(sample_to_slice[2:]) # This prints [30,40,50]
print(sample_to_slice[2:4]) # This prints [30,40]


#----------------------------------------#
# Part 5: Lists are Mutable
# Mutable means it the value could be changed.

sample_to_change = [20, 40, 60, 80]

sample_to_change[0] = sample_to_change[0]+5
sample_to_change[1] = sample_to_change[1]+5
sample_to_change[2] = sample_to_change[2]+5
sample_to_change[3] = sample_to_change[3]+5

print(sample_to_change) # This prints [25, 45, 65, 85]



#----------------------------------------#
# Part 6: Adding & Deleting Elements in a lists


# Adding a single value to a lists using "(list_name).append"

sample_to_add = ["a", "b", "c", "d"]
sample_to_add.append("e")
print(sample_to_add) # This prints ['a', 'b', 'c', 'd', 'e']



# Adding a lists in a lists using "(list_name).extend"

sample_list_1 = [11, 22, 33]
sample_list_2 = [44, 55, 66, 77]

sample_list_1.extend(sample_list_2)
print(sample_list_1) # sample_list_1 now prints [11, 22, 33, 44, 55, 66, 77]


# Deleting a lists value using "del (list_name)[index]"

sample_list_delete = [1, 2, 3, 10]
del sample_list_delete[-1]
print(sample_list_delete) # This only prints [1, 2, 3]



#----------------------------------------#
# Part 7: Using pop on a list.

# sample_list_1 = [11, 22, 33]
# sample_list_2 = [44, 55, 66, 77]

# sample_list_1.extend(sample_list_2)
print(sample_list_1.pop()) # This prints only the "77" if the index is not stated.
# Recommended for printing out he last value in the list quickly.





#----------------------------------------#
# Part 8: Python List Methods

# 1. .append() - Add a value to a list.
# 2. .extend() - Add the value of a list into a list
# 3. .insert() - Insert a value at a given index.
# 4. .remove() - Remove a value in a list at a given index.
# 5. .pop() - Realize a value in a list based on a given index.
# 6. .clear() - Remove all value in a list.
# 7. .copy() - Return a shallow copy of the list.




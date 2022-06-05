# Dictionary: Corresponds to a unique value given by a key
# Age: 25
# Name: Bino



#----------------------------------------#
# Part 1: Accessing a value

from sysconfig import get_path_names


sample_dictionary = {'name': 'Bino', 'age': 25}

get_name = sample_dictionary['name']
print(get_name) # Output: Bino

get_age = sample_dictionary['age']
print(get_age) # Output: 25
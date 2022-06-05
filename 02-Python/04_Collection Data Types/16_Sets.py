# Sets: Is an unordered collection of values.
# Which is unique to one another.
# Which is also immutable.

# Sets uses '{}'



#----------------------------------------#
# Part 1: Creating Set


sample_set = {'a', 'b', 'c', 'd', 'd', 1,}
print(sample_set) #Output: {1, 'd', ,'c', 'b', 'a'} // Randomized


#----------------------------------------#
# Part 2: Adding a value to a set

sample_set1 = {1, 2, 3, 5,} #Output: {1,2,3,5}

sample_set1.add(4)
print(sample_set1) ##Output: {1,2,3,4,5}



#----------------------------------------#
# Part 3: Updating the set values


sample_set2 = {1, 2, 3}
sample_set2.update([4,5,6])
print(sample_set2) #Output: {1,2,3,4,5,6}



#----------------------------------------#
# Part 4: Removing a value from a set

# The discard Function removes the item based on it's unique "value" and not by it's index.

sample_set3 = {1, 2, 3, 4, 5}
sample_set3.discard(1)
print(sample_set3) #Output: {2,3,4,5}



#----------------------------------------#
# Part 5: Combining two sets using : Union

sample_set_a = {'a', 'b', 'c'}
sample_set_b = {1, 2, 3}

sample_sets_result = sample_set_a | sample_set_b
print(sample_sets_result) #Output {1, 2, 3, 'c', 'b', 'a'}

# or we could also use '.union'

sample_sets_result = sample_set_b.union(sample_set_a) 
print(sample_sets_result) #Output {1, 2, 3, 'c', 'b', 'a'}



#----------------------------------------#
# Part 6: Getting the same value of each sets using: Intersection

sample_set_c = {3, 4, 5, 6}
sample_set_d = {5, 6, 7}

sample_sets_intersection = sample_set_c.intersection(sample_set_d)
print(sample_sets_intersection) #Output: {5, 6}



#----------------------------------------#
# Part 7: Getting the difference between sets

sample_sets_difference = sample_set_c.difference(sample_set_d)
print(sample_sets_difference) #Output: {3, 4}
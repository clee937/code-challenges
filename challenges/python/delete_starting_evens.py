# Instructions

# Write a function called delete_starting_evens() that has a parameter named my_list.

# The function should remove elements from the front of my_list until the front of the list is not even. The function should then return my_list.

# For example if my_list started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(my_list) should return [11, 12, 15].

# Make sure your function works even if every element in the list is even!

# ==================================

# 1. Define our function to accept a single input parameter my_list which is a list of numbers
# 2. Loop through every number in the list if there are still numbers in the list and if we haven’t hit an odd number yet
# 3. Within the loop, if the first number in the list is even, then remove the first number of the list
# 4. Once we hit an odd number or we run out of numbers, return the modified list

def delete_starting_evens(my_list):
  while(len(my_list) > 0 and my_list[0] % 2 == 0):
    my_list = my_list[1:]
  return my_list


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
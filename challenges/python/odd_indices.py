# Instructions

# Create a function named odd_indices() that has one parameter named my_list.

# The function should create a new empty list and add every element from my_list that has an odd index. The function should then return this new list.

# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

# ==================================

# 1. Define the function header to accept one input which will be our list of numbers
# 2. Create a new list which will hold our values to return
# 3. Iterate through every odd index until the end of the list
# 4. Within the loop, get the element at the current odd index and append it to our new list
# 5. Return the list of elements which we got from the odd indices.

def odd_indices(my_list):
  new_list = []
  for index in range(1, len(my_list), 2):
    new_list.append(my_list[index])
  return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))

# In our above solution, we iterate through a range of values. The function range(1, len(my_list), 2) returns a list of numbers starting at 1, ending at the length of len(my_list), and incrementing by 2. This causes the loop to iterate through every odd number until the last index of our list of numbers. Using this, we can simply append the element at whatever index we are at since we know that using our range we will be iterating through only odd indices.

# Another way to do this would be to iterate through all indices and use an if statement to see if the index you’re currently looking at is odd, like below:

def odd_indices(my_list):
  new_list = []
  for i in range(len(my_list)):
    if(i % 2 != 0):
      new_list.append(my_list[i])
  return new_list

print(odd_indices([4, 3, 7, 10, 11, -2]))
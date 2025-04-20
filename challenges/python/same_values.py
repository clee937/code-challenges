# Instructions

# Write a function named same_values() that takes two lists of numbers of equal size as parameters. The function should return a list of the indices where the values were equal in lst1 and lst2. For example, "same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])" should return [0, 2, 3].

# =========================================

# Steps

# 1. Define our function to accept two lists of numbers
# 2. Create a new list to store our matching indices
# 3. Loop through each index to the end of either of our lists
# 4. Within the loop, check if our first list at the current index is equal to  the second list at the current index. If so, append the index where they matched.
# 5. Return our list of indices

# ============================================

def same_values(lst1, lst2):
  matching_indices = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      matching_indices.append(index)
  return matching_indices
    

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
# [0, 2, 3]
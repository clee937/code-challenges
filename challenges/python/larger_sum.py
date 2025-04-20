# Codecademy Challenge: [Larger Sum]
# Link: [https://www.codecademy.com/courses/python-for-programmers/articles/advanced-python-code-challenges-loops]


# Instructions:

# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2. The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

# ======================================
# Steps:

# 1. Define the function to accept two input parameters: lst1 and lst2
# 2. Create two variables to record the two sums
# 3. Loop through the first list and add up all of the numbers
# 4. Loop through the second list and add up all of the numbers
# 5. Compare the first and second sum and return the list with the greater sum

# =======================================
# 1)

# def larger_sum(lst1, lst2):
#   sum1 = 0
#   sum2 = 0
#   for num in lst1:
#     sum1 += num
#   for num in lst2:
#     sum2 += num
#   return lst2 if sum2 > sum1 else lst1

# ===================================
# 2)

# def larger_sum(lst1, lst2):
#   sum1 = sum(lst1)
#   sum2 = sum(lst2)
#   return lst2 if sum2 > sum1 else lst1

#  ===================================
# 3)

def larger_sum(lst1, lst2):
  return lst2 if sum(lst2) > sum(lst1) else lst1

print(larger_sum([1, 9, 5], [2, 3, 7]))
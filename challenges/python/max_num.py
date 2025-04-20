# Instructions

# Create a function named max_num() that takes a list of numbers named nums as a parameter. The function should return the largest number in nums.

# ============================================

# Steps

# 1. Define the function to accept a list of numbers called nums
# 2. Set our default maximum value to be the first element in the list
# 3. Loop through every number in the list of numbers
# 4. Within the loop, if we find a number greater than our starting maximum, then replace the maximum with what we found.
# 5. Return the maximum number

# ==============================================

def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if (number > maximum):
      maximum = number
  return maximum

# def max_num(nums):
#   return max(nums)

print(max_num([50, -10, 0, 75, 20])) 
# 75
# Instructions:
# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter. Return the count of how many numbers in the list are divisible by 10.
# ====================================
# 1. Define the function to accept one input parameter called nums
# 2. Initialize a counter to 0
# 3. Loop through every number in nums
# 4. Within the loop, if any of the numbers are divisible by 10, increment our counter
# 5. Return the final counter value

def divisible_by_ten(nums):
  counter = 0
  for number in nums:
    if (number % 10 == 0):
      counter += 1
  return counter

print(divisible_by_ten([20, 25, 30, 35, 40]))
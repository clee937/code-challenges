# CodeWars Challenge: [Odd or Even]
# Link: [https://www.codewars.com/kata/5949481f86420f59480000e7/solutions/python]
# Difficulty: [7 Kyu]

# Instructions
# Given a list of integers, determine whether the sum of its elements is odd or even. Give your answer as a string matching "odd" or "even". If the input array is empty consider it as: [0] (array with a zero).

# Examples
# Input: [0]
# Output: "even"

# Input: [0, 1, 4]
# Output: "odd"

# Input: [0, -1, -5]
# Output: "even"


def oddOrEven(arr):
    return "odd" if sum(arr) % 2 else "even"

# tuple indexing
def oddOrEven(arr):
    return ('even', 'odd')[sum(arr) % 2]

print(oddOrEven([0])) # even
print(oddOrEven([0, 1, 4])) # odd
print(oddOrEven([0, -1, -5])) # even
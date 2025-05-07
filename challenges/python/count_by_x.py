# CodeWars Challenge: [Count by X]
# Link: [https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python]
# Difficulty: [8 Kyu]

# Instructions
# Create a function with two arguments that will return an array of the first n multiples of x. Assume both the given number and the number of times to count will be positive numbers greater than 0. Return the results as an array or list ( depending on language ).

# Examples
# x = 1, n = 10 -> [1,2,3,4,5,6,7,8,9,10]
# x = 2, n = 5  -> [2,4,6,8,10]

def count_by(x, n):
    return list(range(x, x * n + 1, x))

# def count_by(x, n):
#     new_list = []
#     for i in range(1, n+1):
#         new_list.append(i * x)
#     return new_list

# def count_by(x, n):
#     return [i * x for i in range(1, n+1)]
# CodeWars Challenge: [Remove the Minumum]
# Link: [https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python]
# Difficulty: [7 Kyu]
# Instructions:

# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array/list, return an empty array/list. Don't change the order of the elements that are left.

# Examples:
# [1,2,3,4,5] -> [2,3,4,5]
# [5,3,2,1,4] -> [5,3,2,4]
# [2,2,1,2,1] -> [2,2,2,1]

def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    ratings = numbers[:]
    ratings.remove(min(ratings))
    return ratings

# def remove_smallest(numbers):
#     if len(numbers) == 0:
#         return []
#     ratings = numbers.copy()
#     lowest_num = min(numbers)
#     for index in range(len(ratings)):
#         if ratings[index] == lowest_num:
#             ratings.pop(index)
#             return ratings
    
print(remove_smallest([1, 2, 3, 4, 5])) # [2,3,4,5]
print(remove_smallest([5, 3, 2, 1, 4])) # [5,3,2,4]
print(remove_smallest([2, 2, 1, 2, 1])) # [2,2,2,1]
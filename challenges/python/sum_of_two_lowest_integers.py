# CodeWars Challenge: [Sum of two lowest positive integers]
# Link: [https://www.codewars.com/kata/558fc85d8fd1938afb000014/python]
# Difficulty: [7 Kyu]

# Instructions
# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed. For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# Example
# [10, 343445353, 3453445, 3453545353453] should return 3453455.

def sum_two_smallest_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[0] + sorted_numbers[1]


def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))  # --> 7
print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))  # --> 13
print(sum_two_smallest_numbers(
    [10, 343445353, 3453445, 3453545353453]))  # --> 3453455

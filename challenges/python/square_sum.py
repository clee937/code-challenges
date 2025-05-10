# CodeWars Challenge: [Square Sum]
# Link: [https://www.codewars.com/kata/515e271a311df0350d00000f/train/python]
# Difficulty: [8 Kyu]

# Instructions
# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# for loop
def square_sum(numbers):
    sum = 0
    for num in numbers:
        sum += num ** 2
    return sum

# sum()
def square_sum(numbers):
    return sum(num ** 2 for num in numbers)
 
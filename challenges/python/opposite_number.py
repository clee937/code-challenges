# CodeWars Challenge: [Opposite Number]
# Link: [https://www.codewars.com/kata/56dec885c54a926dcd001095/train/python]
# Difficulty: [8 Kyu]

# Instructions
# Given a number, find its opposite (additive inverse).

# Examples:
# 1: -1
# 14: -14
# -34: 34


# Using abs()
def opposite(number):
    return abs(number) if number < 0 else -abs(number)

# Alternatives:
def opposite(number):
    return -number

def opposite(number):
    return number * -1
# CodeWars Challenge: [Round to next 5]
# Link: [https://www.codewars.com/kata/55d1d6d5955ec6365400006d/train/python]
# Difficulty: [7 Kyu]

# Instructions
# Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?

# Examples:
# 0    ->   0
# 2    ->   5
# 3    ->   5
# 12   ->   15
# 21   ->   25
# 30   ->   30
# -2   ->   0
# -5   ->   -5

# More readable
def round_to_next5(n):
    if n % 5 == 0:
        return n

    return (n // 5 + 1) * 5


# More mathematically elegant. This behavior is perfect for rounding to the next multiple of 5, because it always gives us a positive number (0-4) to add, which always moves us forward to the next multiple!
def round_to_next5(n):
    return n + (5-n) % 5


print(round_to_next5(0))  # --> 0
print(round_to_next5(2))  # --> 5
# Parentheses first so 5-2 = 3. 3 % 5 = ? (since 3 / 5 = 0, 3 % 5 = 3). Finally, 2 + 3 = 5.
print(round_to_next5(3))  # --> 5
print(round_to_next5(12))  # --> 15
# 5-12 = -7. Then apply modulo: -7 % 5 = 3. Python's modulo with negatives always gives a positive result. To work this out as 3, count the gap/steps to the next multiple of 5. So from -7 the are 3 steps to reach -10.
print(round_to_next5(21))  # --> 25
print(round_to_next5(30))  # --> 30
print(round_to_next5(-2))  # --> 0
print(round_to_next5(-5))  # --> -5

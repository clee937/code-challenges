# CodeWars Challenge: [Sum of the first nth term of Series]
# Link: [https://www.codewars.com/kata/555eded1ad94b00403000071/train/python]
# Difficulty: [7 Kyu]

# Instructions
# Your task is to write a function which returns the n-th term of the following series, which is the sum of the first n terms of the sequence (n is the input parameter).

# Series
# 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 + ...

# You will need to figure out the rule of the series to complete this.

# Rules
# You need to round the answer to 2 decimal places and return it as a string.
# If the given value is 0 then it should return '0.00'.
# You will only be given Natural Numbers as arguments.

# Examples (Input --> Output)

# n
# 1 --> 1 --> '1.00'
# 2 --> 1 + 1/4 --> '1.25'
# 5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> '1.57'

def series_sum(n):
    return f'{sum(1/d for d in range(1, n*3, 3)):.2f}'


def series_sum(n):
    result = 0

    for d in range(1, n*3, 3):
        result += 1/d

    return f'{result:.2f}'


print(series_sum(0))  # --> '0.00'
print(series_sum(1))  # --> '1.00'
print(series_sum(2))  # --> '1.25'
print(series_sum(3))  # --> '1.39'
print(series_sum(5))  # --> '1.57'

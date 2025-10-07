# CodeWars Challenge: [Write number in expanded form]
# Link: [https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python]
# Difficulty: [6 Kyu]

# Instructions
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# 12 --> "10 + 2"
# 45 --> "40 + 5"
# 70304 --> "70000 + 300 + 4"

# Using string manipulation
def expanded_form(num):
    result = list()
    length = len(str(num)) - 1
    for char in str(num):
        if char != '0':
            result.append(char + length * '0')
        length -= 1
    return ' + '.join(result)


def expanded_form(num):
    result = []
    num_str = str(num)
    for i, digit in enumerate(num_str):
        if digit != '0':
            place_value = digit + '0' * (len(num_str) - i - 1)
            result.append(place_value)
    return ' + '.join(result)


# List comprehension
def expanded_form(num):
    num_str = str(num)
    return ' + '.join([
        digit + '0' * (len(num_str) - i - 1)
        for i, digit in enumerate(num_str)
        if digit != '0'
    ])


# Using maths (more explicit)
def expanded_form(num):
    num_str = str(num)
    length = len(num_str)
    result = []

    for i, digit in enumerate(num_str):
        if digit != '0':
            power = length - i - 1
            place_value = int(digit) * (10 ** power)
            result.append(str(place_value))

    return ' + '.join(result)


# Reversed string approach
def expanded_form(num):
    result = []
    multiplier = 1

    while num > 0:
        digit = num % 10  # Get last digit
        if digit != 0:
            result.append(str(digit * multiplier))
        num //= 10  # Remove last digit
        multiplier *= 10

    return ' + '.join(reversed(result))


print(expanded_form(12))  # --> "10 + 2"
print(expanded_form(45))  # --> "40 + 5"
print(expanded_form(70304))  # --> "70000 + 300 + 4"

# CodeWars Challenge: [Square Every Digit]
# Link: [https://www.codewars.com/kata/546e2562b03326a88e000020/train/python]
# Difficulty: [7 Kyu]

# Instructions
# In this kata, you are asked to square every digit of a number and concatenate them. For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81).

# Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

# Note: The function accepts an integer and returns an integer.

# 1
def square_digits(num):
    result = ''
    for number in str(num):
        number_squared = int(number) ** 2
        result += str(number_squared)
    return int(result)

# 2
def square_digits(num):
    result = ''
    for number in str(num):
        result += str(int(number) ** 2)
    return int(result)

# 3
def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

print(square_digits(9119))
print(square_digits(765))
print(square_digits(0))
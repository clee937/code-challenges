# CodeWars Challenge: [Fake Binary]
# Link: [https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python]
# Difficulty: [8 Kyu]

# Instructions
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

# for loop
def fake_bin(x):
    new_string = ''
    for number in x:
        if int(number) < 5:
            new_string += '0'
        else:
            new_string += '1'
    return new_string

# join()
def fake_bin(x):
    return ''.join('0' if int(number) < 5 else '1' for number in x)


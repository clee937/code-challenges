# CodeWars Challenge: [Remove an exclamation mark]
# Link: [https://www.codewars.com/kata/57fae964d80daa229d000126/train/python]
# Difficulty: [8 Kyu]

# Instructions
# Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.

# Examples:
# 'Hi!'     --> 'Hi'
# 'Hi!!!'  --> 'Hi!!'
# '!Hi'    --> '!Hi'
# '!Hi!'    --> '!Hi'
# 'Hi! Hi!' --> 'Hi! Hi'
# 'Hi'      --> 'Hi'


# Most concise and readable. Built-in method for exactly this purpose. Handles empty strings automatically. Explicitly states intent. Requires Python 3.9+
def remove(s):
    return s.removesuffix('!')


def remove(s):
    return s[:-1] if s.endswith('!') else s


def remove(s):
    return s[:-1] if (s and s[-1] == '!') else s


print(remove('Hi!'))  # --> 'Hi'
print(remove('Hi!!!'))  # --> 'Hi!!'
print(remove('!Hi'))  # --> '!Hi'
print(remove('!Hi!'))  # --> '!Hi'
print(remove('Hi! Hi!'))  # --> 'Hi! Hi'
print(remove('Hi'))  # --> 'Hi'
print(remove(''))  # --> ''

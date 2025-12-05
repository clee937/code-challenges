# CodeWars Challenge: [Get character from ASCII Value]
# Link: [https://www.codewars.com/kata/55ad04714f0b468e8200001c/train/python]
# Difficulty: [8 Kyu]

# Instructions
# Write a function which takes a number and returns the corresponding ASCII char for that value.

# Example:
# 65 --> 'A'
# 97 --> 'a'
# 48 --> '0

# 1. Simple, clear, Pythonic. Built-in function designed for this purpose.
def get_char(c):
    return chr(c)


# Old style string formatting but still valid
def get_char(c):
    return '%c' % c


print(get_char(65))  # --> 'A'
print(get_char(97))  # --> 'a'
print(get_char(48))  # --> '0'
print(get_char(33))  # --> '!'
print(get_char(34))  # --> '"'
print(get_char(35))  # --> '#'
print(get_char(36))  # --> '$'
print(get_char(37))  # --> '%'
print(get_char(38))  # --> '&'

# CodeWars Challenge: [Isograms]
# Link: [https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python]
# Difficulty: [7 Kyu]

# Instructions:
# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example:
# "Dermatoglyphics" -> true
# "aba" -> false
# "moOse" -> false (ignore letter case)

def is_isogram(string):
    return len(string) == len(set(string.lower()))

# More efficient for longer words
def is_isogram(string):
    return len(string) == len(set(string.lower())) if len(string) <= 26 else False

def is_isogram(string):
    lowercase_string = string.lower()
    for char in lowercase_string:
        if lowercase_string.count(char) > 1: return False
    return True
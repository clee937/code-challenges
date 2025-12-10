# CodeWars Challenge: [Is the string uppercase?]
# Link: [https://www.codewars.com/kata/56cd44e1aa4ac7879200010b/train/python]
# Difficulty: [8 Kyu]

# Instructions
# Create a method to see whether the string is ALL CAPS. In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string containing no letters at all is trivially considered to be in ALL CAPS.

# Examples (input -> output)

# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True

def is_uppercase(string):
    return string.upper() == string


def is_uppercase(string):
    for char in string:
        if char.islower():
            return False
    return True


print(is_uppercase('c'))  # --> False
print(is_uppercase('C'))  # --> True
print(is_uppercase('hello I AM DONALD'))  # --> False
print(is_uppercase('HELLO I AM DONALD'))  # --> True
print(is_uppercase('$%&'))  # --> True

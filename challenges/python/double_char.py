# CodeWars Challenge: [Double Char]
# Link: [https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python]
# Difficulty: [8 Kyu]

# Instructions
# Given a string, create a function that returns a string in which each character (case-sensitive) is repeated once.

# Examples:
# "String"      -> "SSttrriinngg"
# "Hello World" -> "HHeelllloo  WWoorrlldd"
# "1234!_ "     -> "11223344!!__  "

# join() 
def double_char(string):
    return ''.join(character * 2 for character in string)

# for loop
def double_char(s):
    new_string = ''
    for letter in s:
        new_string += letter * 2
    return new_string
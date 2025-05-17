# CodeWars Challenge: [Replace with Alphabet Position]
# Link: [https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python]
# Difficulty: [6 Kyu]

# Instructions
# In this kata you are required to, given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it.

# Examples
# "a" = 1, "b" = 2, etc.
# Input = "The sunset sets at twelve o' clock."
# Output = "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"

# 1.
def alphabet_position(text):
    return ' '.join(str(ord(char) - 96) for char in text.lower() if char.isalpha())
# 2.
def alphabet_position(text):
    text_to_check = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    position_list = []
    for char in text_to_check:
        if char in alphabet:
            position_list.append(str(alphabet.index(char)+1))
    return ' '.join(position_list)

# 3. With string import and ascii_lowercase
from string import ascii_lowercase

def alphabet_position(text):
    text_to_check = text.lower()
    alphabet = ascii_lowercase
    position_list = []
    for char in text_to_check:
        if char in alphabet:
            position_list.append(str(alphabet.index(char)+1))
    return ' '.join(position_list)

# 4. Using isalpha() and ord(). ord() returns the unicode code point (integer representation) of a single character). "-96" to get alphabet position for lowercase. "-64" for uppercase.
def alphabet_position(text):
    lowercase_text = text.lower()
    position_list = []
    for char in lowercase_text:
        if char.isalpha():
            position_list.append(str(ord(char) - 96))
    return ' '.join(position_list)
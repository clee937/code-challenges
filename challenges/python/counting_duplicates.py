# CodeWars Challenge: [Counting Duplicates]
# Link: [https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/train/python]
# Difficulty: [6 Kyu]

# Instructions:
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# Example:
# "abcde" -> 0
# "aabbcde" -> 2 ('a' and 'b')
# "aabBcde" -> 2 ('a' and 'b')
# "indivisibility" -> 1 ('i' occurs 6 times)
# "aA11" -> 2 ('a' and 'i')
# "ABBA" -> 2 ('A' and 'B')

# using dictionary
def duplicate_count(text):
    letter_count = {}
    count = 0
    
    for letter in text.lower():
        if letter not in letter_count:
            letter_count[letter] = 1
        else: letter_count[letter] += 1
    
    for value in letter_count.values():
        if value > 1:
            count += 1
    return count

# def duplicate_count(text):
#     char_count = 0
#     for char in set(text.lower()):
#         if text.lower().count(char) > 1:
#             char_count += 1
#     return char_count

# list comprehension
# def duplicate_count(text):
#     return len([char for char in set(text.lower()) if text.lower().count(char) > 1])


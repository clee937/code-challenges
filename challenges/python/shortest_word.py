# CodeWars Challenge: [Shortest Word]
# Link: [https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python]
# Difficulty: [7 Kyu]

# Instructions
# Simple, given a string of words, return the length of the shortest word(s).String will never be empty and you do not need to account for different data types.


def find_short(s):
    return min(len(word) for word in s.split())


def find_short(s):
    return len(min(s.split(), key=len))

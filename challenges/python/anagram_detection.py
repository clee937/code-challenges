# CodeWars Challenge: [Anagram Detection]
# Link: [https://www.codewars.com/kata/529eef7a9194e0cbc1000255/train/python]
# Difficulty: [7 Kyu]

# Instructions
# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia). Note: anagrams are case insensitive

# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

# Examples
# "foefet" is an anagram of "toffee"
# "Buckethead" is an anagram of "DeathCubeK"

def is_anagram(test, original):
    return sorted(list(test.lower())) == sorted(list(original.lower()))


print(is_anagram("foefet", "toffee"))  # --> True
print(is_anagram("Buckethead", "DeathCubeK"))  # --> True
print(is_anagram("Twoo", "WooT"))  # --> True
print(is_anagram("dumble", "bumble"))  # --> False
print(is_anagram("apple", "pale"))  # --> False

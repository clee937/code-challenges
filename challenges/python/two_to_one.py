# CodeWars Challenge: [Two to One]
# Link: [https://www.codewars.com/kata/5656b6906de340bd1b0000ac/python]
# Difficulty: [7 Kyu]

# Instructions
# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string (alphabetical ascending), the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    pass


print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))  # --> "abcdefklmopqwxy"
print(longest("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"))
# --> "abcdefghijklmnopqrstuvwxyz"

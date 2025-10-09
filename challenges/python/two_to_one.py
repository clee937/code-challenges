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

# String concatenation creates an entirely new string in memory. For very long strings, will require extra memory.
def longest(s1, s2):
    return ''.join(sorted(set(s1 + s2)))


# Union operator combines 2 sets (just references, not string data). Set operations are optimised.
def longest(s1, s2):
    return ''.join(sorted(set(s1) | set(s2)))


print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))  # --> "abcdefklmopqwxy"
print(longest("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"))
# --> "abcdefghijklmnopqrstuvwxyz"
print(longest("aretheyhere", "yestheyarehere"))  # --> "aehrsty"

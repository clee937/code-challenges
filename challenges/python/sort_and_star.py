# CodeWars Challenge: [Sort and Star]
# Link: [https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python]
# Difficulty: [8 Kyu]

# Instructions
# You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value. The returned value must be a string, and have "***" between each of its letters. You should not remove or add elements from/to the array.

def two_sort(lst):
    return "***".join(min(lst))

# sorts whole list unecessarily
# def two_sort(lst):
#     return "***".join(sorted(lst)[0])


# ----------------------------------------
# About next() with generator expression
# Without next() - processes ALL words
result = ['***'.join(w) for w in sorted(array)][0]

# With next() - only processes the FIRST word. The benefit: Once next() gets the first item, the generator stops. It doesn't join all the other words unnecessarily. However, this still has to sort the entire array first - Not ideal because that's the expensive part.
result = next('***'.join(w) for w in sorted(array))

# The next(generator) pattern is useful when:
# - You're filtering and want the first match
# - The expensive operation is inside the generator, not before it
# Example where it shines:

# Find first even number > 100 without processing all numbers
result = next(x for x in huge_list if x > 100 and x % 2 == 0)


print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe",
      "who", "knows", "perhaps"]))  # -->  'b***i***t***c***o***i***n'
print(two_sort(["turns", "out", "random", "test", "cases", "are", "easier",
      "than", "writing", "out", "basic", "ones"]))  # -->  'a***r***e'
print(two_sort(["lets", "talk", "about", "javascript", "the",
      "best", "language"]))  # -->  'a***b***o***u***t'
print(two_sort(["i", "want", "to", "travel", "the", "world",
      "writing", "code", "one", "day"]))  # -->  'c***o***d***e'
print(two_sort(["Lets", "all", "go", "on", "holiday",
      "somewhere", "very", "cold"]))  # -->  'L***e***t***s'

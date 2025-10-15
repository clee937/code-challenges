# Codecademy Challenge: [Count Multi X]
# Link: [https://www.codecademy.com/courses/learn-python-3/articles/python-code-challenges-strings]
# Difficulty: [8 Kyu]

# Instructions:
# Write a function named count_multi_char_x that takes a string named 'word' and a string named 'x'. It should return the number of times x appears in word.

# Example:
# count_multi_char_x("Mississippi", "iss") --> 2

# Using split()
def count_multi_char_x(word, x):
    splits = word.split(x)
    # print(splits)
    # if 2 substrings are directly adjacent, split() creates an empty space element in the list/array
    return len(splits)-1

# Using count()
# def count_multi_char_x(word, x):
#     return word.count(x)


print(count_multi_char_x("Mississippi", "iss"))  # --> 2
print(count_multi_char_x("apple", "pp"))  # --> 1

# Codecademy Challenge: [Frequency Dictionary]
# Link: [https://www.codecademy.com/courses/learn-python-3/articles/advanced-python-code-challenges-dictionaries]
# Difficulty: [7 Kyu]

# Instructions:
# Write a function named frequency_dictionary that takes a list of elements named words as a parameter. The function should return a dictionary containing the frequency of each element in words.


# def frequency_dictionary(words):
#     dict = {}
#     for word in words:
#         dict[word] = dict.get(word, 0) + 1
#     return dict


# def frequency_dictionary(words):
#     dict = {}
#     for word in words:
#         if word not in dict:
#             dict[word] = 0
#         dict[word] += 1
#     return dict

from collections import Counter


# Alternative using Counter. Built-in and optimised
def frequency_dictionary(words):
    return Counter(words)


print(frequency_dictionary(["apple", "apple", "cat", 1]))
# --> {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0]))
# --> should print {0:5}

# Codecademy Challenge: [Reverse String]
# Link: [https://www.codecademy.com/courses/learn-python-3/articles/advanced-python-code-challenges-strings]
# Difficulty: [7 Kyu]

# Instructions:
# Write a function named reverse_string that has a string named word as a parameter. The function should return word in reverse.

# def reverse_string(word):
#     reversed_word = ''
#     for i in range(len(word)-1, -1, -1):
#         reversed_word += word[i]
#     return reversed_word

def reverse_string(word):
    return ''.join(reversed(word))


print(reverse_string('Codecademy'))  # --> ymedacedoC
print(reverse_string('Hello world!'))  # --> !dlrow olleH
print(reverse_string(''))  # --> ''

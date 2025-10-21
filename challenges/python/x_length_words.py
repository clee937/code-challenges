# Codecademy Challenge: [X-Length-Words]
# Link: [https://www.codecademy.com/courses/learn-python-3/articles/python-code-challenges-strings]
# Difficulty: [8 Kyu]

# Instructions:
# Create a function called x_length_words that takes a string named sentence and an integer named x as parameters. This function should return True if every word in sentence has a length greater than or equal to x.

# Example:
# x_length_words("i like apples", 2) --> False

def x_length_words(sentence, x):
    words = sentence.split()
    for word in words:
        if len(word) < x:
            return False
    return True


print(x_length_words("i like apples", 2))  # --> False
print(x_length_words("he likes apples", 2))  # --> True

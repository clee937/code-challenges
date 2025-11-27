# CodeWars Challenge: [Add Length]
# Link: [https://www.codewars.com/kata/559d2284b5bb6799e9000047/train/python]
# Difficulty: [8 Kyu]

# Instructions
# Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .

# Note: String will have at least one element; words will always be separated by a space.

# Example (Input --> Output)
# "apple ban" --> ["apple 5", "ban 3"]
# "you will win" --> ["you 3", "will 4", "win 3"]

# List comprehension
def add_length(str_):
    return [f'{word} {len(word)}' for word in str_.split()]


def add_length(str_):
    list_of_words = str_.split()
    result = []

    for word in list_of_words:
        result.append(f'{word} {len(word)}')

    return result


print(add_length('apple ban'))  # --> ['apple 5', 'ban 3']
print(add_length('you will win'))  # --> ['you 3', 'will 4', 'win 3']
print(add_length('you'))  # --> ['you 3']
print(add_length('y'))  # --> ["y 1"]

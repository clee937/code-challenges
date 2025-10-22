# Codecademy Challenge: [Unique Values]
# Link: [https://www.codecademy.com/courses/learn-python-3/articles/advanced-python-code-challenges-dictionaries]
# Difficulty: [7 Kyu]

# Instructions:
# Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. The function should return the number of unique values in the dictionary.

def unique_values(my_dictionary):
    return len(set(my_dictionary.values()))


def unique_values(my_dictionary):
    uniques = []
    for value in my_dictionary.values():
        if value not in uniques:
            uniques.append(value)
    return len(uniques)


print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
# --> 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
# --> 1

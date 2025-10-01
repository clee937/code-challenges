# CodeWars Challenge: [Removing elements]
# Link: [https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python]
# Difficulty: [8 Kyu]

# Instructions
# Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

# Examples
# ['Hello', 'Goodbye', 'Hello Again'] --> ['Hello', 'Hello Again']
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] --> [1, 3, 5, 7, 9]
# [[1, 2]] --> [[1, 2]]
# [['Goodbye'], {'Great': 'Job'}]) --> [['Goodbye']]

# List slicing. Most pythonic. Avoids mutation.
def remove_every_other(my_list):
    return my_list[::2]


def remove_every_other(my_list):
    # Create a new list. List comprehension.
    return [my_list[i] for i in range(0, len(my_list), 2)]


def remove_every_other(my_list):
    # Iterate backwards. Removing later indices doesn't affect earlier ones
    for i in range(len(my_list)-1, 0, -2):
        my_list.pop(i)
    return my_list


print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
# --> ['Hello', 'Hello Again']
print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# --> [1, 3, 5, 7, 9]
print(remove_every_other([[1, 2]]))  # --> [[1, 2]]
print(remove_every_other([['Goodbye'], {'Great': 'Job'}]))  # --> [['Goodbye']]

# CodeWars Challenge: [You only need one]
# Link: [https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python]
# Difficulty: [8 Kyu]

# Instructions
# You will be given an array 'a' and a value 'x'. Check whether the provided array contains the value. 'a' can contain numbers or strings. 'x' can be either. Return true if the array contains the value, false if not.

# using 'in' operator
def check(seq, elem):
    return elem in seq

# using for loop
def check(seq, elem):
    for element in seq:
        if elem == element:
            return True
    return False
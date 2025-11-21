# CodeWars Challenge: [Sum Mixed Array]
# Link: [https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python]
# Difficulty: [8 Kyu]

# Instructions
# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers. Return your answer as a number.


# Generator expression. Overhead performance cost from if/else statement for typechecking/branching
def sum_mix(arr):
    return sum(num if type(num) == int else int(num) for num in arr)


# int(5) when 5 is already an int is extremely fast — it just returns the same object. Python's int() is optimized in C and recognizes when conversion isn't needed. The "always convert" approach is typically 10-20% faster because the overhead of the conditional check in the solution above exceeds the cost of the (nearly free) int conversion.
def sum_mix(arr):
    return sum(int(num) for num in arr)


# Functional approach. map() is slightly faster - built-in function (implemented in C - low level code. Fast.) - no overhead from Python loop. More memory efficient for large arrays. Most concise/elegant.
def sum_mix(arr):
    return sum(map(int, arr))

# map(int, arr) - Creates a map object that will apply the int() function to each element in arr. This is lazy evaluation — it doesn't actually convert anything yet, just creates an iterator. sum(...) - Consumes the map object, triggering the conversions. As sum() iterates, map applies int() to each element one by one.

# Why is map() faster?
# The map() function is implemented in C, so the looping happens at C speed. A Python list comprehension loops in Python bytecode, which is slower.


print(sum_mix([9, 3, '7', '3']))  # --> 22
print(sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]))  # --> 42
print(sum_mix(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']))  # --> 41

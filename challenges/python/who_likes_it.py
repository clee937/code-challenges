# CodeWars Challenge: [Who likes it?]
# Link: [https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python]
# Difficulty: [6 Kyu]

# Instructions
# Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples. For 4 or more names, the number in "and 2 others" simply increases.

# Examples
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

# Using match statement and * for unpacking.
# Python 3.10+ introduced structural pattern matching, which allows us to match the shape and contents of a list directly.
# match names: is not matching the value of names per se — it's checking the structure of the list:
# []: an empty list
# [a]: a list with one element
# [a, b]: two elements
# [a, b, c]: three elements
# [a, b, *rest]: at least two elements, where rest captures the remainder
# So Python is deconstructing the list based on its content and length — which is more expressive than just checking .length if doing this in TypeScript
def likes(names):
    match names:
        case []: return 'no one likes this'
        case [a]: return f'{a} likes this'
        case [a, b]: return f'{a} and {b} like this'
        case [a, b, c]: return f'{a}, {b} and {c} like this'
        case [a, b, *rest]: return f'{a}, {b} and {len(rest)} others like this'

# def likes(names):
#     if len(names) == 0:
#         return f'no one likes this'
#     if len(names) == 1:
#         return f'{names[0]} likes this'
#     if len(names) == 2:
#         return f'{names[0]} and {names[1]} like this'
#     if len(names) == 3:
#         return f'{names[0]}, {names[1]} and {names[2]} like this'
#     if len(names) >= 4:
#         return f'{names[0]}, {names[1]} and {len(names)-2} others like this'

# using dictionary
# def likes(names):
#     formats = {
#             0: "no one likes this",
#             1: "{} likes this",
#             2: "{} and {} like this",
#             3: "{}, {} and {} like this",
#             4: "{}, {} and {others} others like this"
#         }
#     n = len(names)
#     return formats[min(n,4)].format(*names, others=n-2)

print(likes([])) # "no one likes this"
print(likes(["Peter"] ))  # "Peter likes this"
print(likes(["Jacob", "Alex"]))  # "Jacob and Alex like this"
print(likes(["Max", "John", "Mark"]))  # "Max, John and Mark like this"
print(likes(["Alex", "Jacob", "Mark", "Max"]))  # "Alex, Jacob and 2 others like this"

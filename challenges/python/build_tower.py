# CodeWars Challenge: [Build Tower]
# Link: [https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python]
# Difficulty: [6 Kyu]

# Instructions
# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

# For example, a tower with 3 floors looks like this:

# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]
# And a tower with 6 floors looks like this:

# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]

def tower_builder(n_floors):
    width = 2 * n_floors - 1
    return [('*' * (2*level+1)).center(width) for level in range(n_floors)]


# center()
def tower_builder(n_floors):
    tower_list = []
    for i in range(1, n_floors+1):
        width = i * 2 - 1
        spaces = (n_floors-i)*2
        tower_list.append(
            ('*' * width).center(width + spaces))
    return tower_list


# def tower_builder(n_floors):
#     return [f"{' ' * (n_floors-i)}{'*' * (i * 2 - 1)}{' ' * (n_floors-i)}" for i in range(1, n_floors+1)]


# def tower_builder(n_floors):
#     tower_list = []
#     for i in range(1, n_floors+1):
#         tower_list.append(
#             f"{' ' * (n_floors-i)}{'*' * (i * 2 - 1)}{' ' * (n_floors-i)}")
#     return tower_list


print(tower_builder(3))
print(tower_builder(6))

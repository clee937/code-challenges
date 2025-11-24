# CodeWars Challenge: [Give me a diamond]
# Link: [https://www.codewars.com/kata/5503013e34137eeeaa001648/train/python]
# Difficulty: [6 Kyu]

# Instructions
# Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help. You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

# Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.

# Examples
# A size 3 diamond:

#  *
# ***
#  *

# ...which would appear as a string of ' *\n***\n *\n'

# A size 5 diamond:

#   *
#  ***
# *****
#  ***
#   *

# ...that is:

# '  *\n ***\n*****\n ***\n  *\n'


# Builds from top down. Builds top half and then mirrors it.
def diamond(size):
    if size % 2 == 0 or size < 0:
        return None

    lines = []

    for i in range(1, size + 1, 2):
        spaces = ' ' * ((size - i) // 2)
        stars = '*' * i
        lines.append(f'{spaces}{stars}\n')

    return ''.join(lines) + ''.join(lines[-2::-1])


# List comprehension of the above
def diamond(size):
    if size % 2 == 0 or size < 0:
        return None

    lines = [' ' * ((size - i) // 2) + '*' * i + '\n'
             for i in range(1, size + 1, 2)]

    return ''.join(lines + lines[-2::-1])


# Builds from inside out. Starts in middle and builds outward. Wraps each new row around the existing diamond. Less readable, performant, Pythonic than first solution.
def diamond(n):
    if n < 0 or n % 2 == 0:
        return None

    result = '*' * n + '\n'
    spaces = 1
    n = n - 2
    while n > 0:
        current = ' ' * spaces + '*' * n + '\n'
        spaces = spaces + 1
        n = n - 2
        result = current + result + current

    return result


print(diamond(1))  # --> '*\n'
print(diamond(2))  # --> None
print(diamond(3))  # --> '  *\n***\n *\n'
print(diamond(5))  # --> '  *\n ***\n*****\n ***\n  *\n'
print(diamond(0))  # --> None
print(diamond(-3))  # --> None

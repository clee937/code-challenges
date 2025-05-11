# CodeWars Challenge: [Abbreviate a Two Word Name]
# Link: [https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python]
# Difficulty: [8 Kyu]

# Instructions
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them. The output should be two capital letters with a dot separating them.

# Examples
# Sam Harris -> S.H
# patrick feeney -> P.F

# 1
def abbrev_name(name):
    name_list = name.split()
    return f'{name_list[0][0]}.{name_list[1][0]}'.upper()

# 2
def abbrev_name(name):
    name_list = name.split()
    result = []
    for name in name_list:
        result.append(name[0].upper())
    return '.'.join(result)


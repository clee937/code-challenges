# CodeWars Challenge: [Mumbling]
# Link: [https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python]
# Difficulty: [7 Kyu]

# Instructions
# This time no story, no theory. The examples below show you how to write function accum. The parameter of accum is a string which includes only letters from a..z and A..Z.

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

# def accum(string):
#     new_string = ''
#     for index in range(len(string)):
#         new_string += f'{string[index] * (index + 1)}-'.title()
#     return new_string.rstrip("-")

# def accum(string):
#     count = 0
#     string_array = []
#     for letter in string:
#         string_array.append(f'{letter.upper()}{letter.lower() * count}')
#         count += 1
#     return '-'.join(string_array)

# enumerate() takes a collection and returns it as an enumerate object. It adds a counter as the key of the enumerate object. 
# eg. enumerate(iterable, start)

def accum(string):
    return '-'.join(char.upper() + char.lower() * index for index, char in enumerate(string))
    
        
print(accum("abcd"))   # "A-Bb-Ccc-Dddd"
print(accum("RqaEzty"))  # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
print(accum("cwAt"))   # "C-Ww-Aaa-Tttt"


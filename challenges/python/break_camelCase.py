# CodeWars Challenge: [Break camelCase]
# Link: [https://www.codewars.com/kata/5208f99aee097e6552000148/train/python]
# Difficulty: [6 Kyu]

# Instructions
# Complete the solution so that the function will break up camel casing, using a space between words.

# Example

# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    separated_words = ''
    for char in s:
        if char.isupper():
            separated_words += ' ' + char
        else:
            separated_words += char
    return separated_words


def solution(s):
    return ''.join(' ' + char if char.isupper() else char for char in s)


print(solution('camelCasing'))  # => 'camel Casing'
print(solution('identifier'))  # => 'identifier'
print(solution(''))  # => ''
print(solution('breakCamelCase'))  # => 'break Camel Case'

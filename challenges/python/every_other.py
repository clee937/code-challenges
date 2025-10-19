# Codecademy Challenge: [Every Other]
# Link: [https://www.codecademy.com/courses/learn-python-3/articles/advanced-python-code-challenges-strings]
# Difficulty: [7 Kyu]

# Instructions:
# Create a function named every_other_letter that takes a string named word as a parameter. The function should return a string containing every other letter in word.


def every_other_letter(word):
    return word[::2]


def every_other_letter(word):
    every_other = ''
    for i, char in enumerate(word):
        if i % 2 == 0:
            every_other += char
    return every_other


def every_other_letter(word):
    every_other = ''
    for i in range(0, len(word), 2):
        every_other += word[i]
    return every_other


def every_other_letter(word):
    every_other = ''
    for i in range(len(word)):
        if not i % 2:
            every_other += word[i]
    return every_other


'''
if not (i % 2):
stops at indices of even values
Does NOT mean: "if i is not divisible by 2"
Actually means: "if the remainder of i÷2 is falsy (i.e., equals 0)"
If the remainder isn't 1, then statement is truthy/equals True. If the remainder isn't odd then statement is truthy/equals True.
If not True (ie. If not 1).

word = "h e l l o"
index: 0 1 2 3 4

i % 2:    0 1 0 1 0  (remainder when divided by 2)
not i%2:  T F T F T  (flip 0→True, 1→False)
select:   ✓ ✗ ✓ ✗ ✓
'''


print(every_other_letter('Codecademy'))
# --> 'Cdcdm'
print(every_other_letter('Hello world!'))
# --> 'Hlowrd'
print(every_other_letter(''))
# -- ''

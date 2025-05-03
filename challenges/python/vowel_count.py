# CodeWars Challenge: [Vowel Count]
# Link: [https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python]
# Difficulty: [7 Kyu]

# Instructions
# Return the number (count) of vowels in the given string. We will consider a, e, i, o, u as vowels for this Kata (but not y). The input string will only consist of lower case letters and/or spaces.

# for loops
def get_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in string:
        for vowel in vowels:
            if letter == vowel:
                count += 1
    return count


def get_count(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in string:
        # if letter in 'aeiou':
        if letter in vowels:
                count += 1
    return count

# generator expression
def get_count(string):
    return sum(1 for letter in string if letter in "aeiouAEIOU")

# list comprehension
def get_count(string):
    return sum(char in 'aeiou' for char in string)

def get_count(string):
    # return sum(string.count(char) for char in ['a', 'e', 'i', 'o', 'u'])
	return sum(string.count(char) for char in 'aeiou')

def get_count(string):
	count = 0
	for letter in 'aeiou':
		count += string.count(letter)
	return count

# creates a list of vowels and returns the length of the list. For letter(x) in string, if letter(x) is in 'aeiou', add it to the list, and return the length of the list

def get_count(string):
    return len([letter for letter in string if letter in 'aeoiu'])


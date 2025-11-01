# CodeWars Challenge: [Detect Pangram]
# Link: [https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python]
# Difficulty: [6 Kyu]

# Instructions
# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant). Given a string, detect whether or not it is a pangram. Return True if it is , False if not. Ignore numbers and punctuation.


def is_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower_case_string = string.lower()
    for char in alphabet:
        if char not in lower_case_string:
            return False
    return True


def is_pangram(string):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')

    for char in string.lower():
        alphabet.discard(char)

    return len(alphabet) == 0


# all() checks all conditions are true. Generator expression for each letter.
def is_pangram(string):
    string_lower = string.lower()
    return all(char in string_lower for char in 'abcdefghijklmnopqrstuvwxyz')


# Most Pythonic
def is_pangram(string):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(string.lower())


print(is_pangram('The quick brown fox jumps over the lazy dog.'))  # True
print(is_pangram('Cwm fjord bank glyphs vext quiz'))  # True
print(is_pangram('Pack my box with five dozen liquor jugs.'))  # True
print(is_pangram('How quickly daft jumping zebras vex.'))  # True
print(is_pangram('ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ'))  # True
print(is_pangram('This isn\'t a pangram!'))  # False
print(is_pangram('abcdefghijklm opqrstuvwxyz'))  # False
print(is_pangram('Aacdefghijklmnopqrstuvwxyz'))  # False

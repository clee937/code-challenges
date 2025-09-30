# CodeWars Challenge: [Duplicate Encoder]
# Link: [https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python]
# Difficulty: [6 Kyu]

# Instructions
# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

# =======================================================

def duplicate_encode(word):
    word = word.lower()
    # word.count() being called for every char is not the most efficient
    return ''.join(')' if word.count(char) > 1 else '(' for char in word)

# =======================================================

from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    word_count = Counter(word)
    
    return ''.join('(' if word_count[char] == 1 else ')' for char in word)

# =======================================================

from collections import defaultdict
# Initialise the counter using a defaultdict with int() as a default factory function. This way, when we access a key that doesn’t exist, the dictionary automatically creates the key and initializes it with the value that the factory function returns. In this case, int() as a factory function, without arguments returns 0.

def duplicate_encode(word):
    word = word.lower()
    word_count = defaultdict(int)
    
    for char in word:
        word_count[char] += 1

    return ''.join('(' if word_count[char] == 1 else ')' for char in word)
    
# =======================================================

def duplicate_encode(word):
    word = word.lower()
    dict = {}
    for char in word:
        dict[char] = dict.get(char, 0) + 1
        
    return ''.join('(' if dict[char] == 1 else ')' for char in word)

# =======================================================

def duplicate_encode(word):
    word = word.lower()
    
    dict = {}
    for char in word:
        dict[char] = ')' if char in dict else '('
    
    return ''.join(dict[char] for char in word)

# =======================================================

print(duplicate_encode("din")) # =>  "((("
print(duplicate_encode("recede")) # =>  "()()()"
print(duplicate_encode("Success")) # =>  ")())())"
print(duplicate_encode("(( @")) # =>  "))(("
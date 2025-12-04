# CodeWars Challenge: [Complementary DNA]
# Link: [https://www.codewars.com/kata/554e4a2f232cdd87d9000038/solutions/python]
# Difficulty: [7 Kyu]

# Instructions
# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

# If you want to know more: http://en.wikipedia.org/wiki/DNA

# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA; you need to return the other complementary side. DNA strand is never empty or there is no DNA at all.

# Examples:
# 'ATTGC' --> 'TAACG'
# 'GTAT' --> 'CATA'


# Uses Python's built-in string translation feature. Most efficient - translate() is implemented in C, very fast. Pythonic - leverages the right tool for the job. Most concise - one line, no loops.
def dna_strand(dna):
    return dna.translate(str.maketrans("ATCG", "TAGC"))


# dictionary and generator
def dna_strand(dna):

    dna_letters = {
        'T': 'A',
        'A': 'T',
        'G': 'C',
        'C': 'G'
    }

    return ''.join(dna_letters[letter] for letter in dna)


def dna_strand(dna):

    dna_letters = {
        'T': 'A',
        'A': 'T',
        'G': 'C',
        'C': 'G'
    }

    result = []

    for letter in dna:
        result.append(dna_letters[letter])

    return ''.join(result)


# def dna_strand(dna):

#     dna_letters = {
#         'T': 'A',
#         'A': 'T',
#         'G': 'C',
#         'C': 'G'
#     }

#     result = ''

#     for letter in dna:
#         result += dna_letters[letter]

#     return result

print(dna_strand('ATTGC'))  # --> 'TAACG'
print(dna_strand('GTAT'))  # --> 'CATA'
print(dna_strand('AAAA'))  # --> 'TTTT'


# ===================================================
# str.maketrans("ATCG", "TAGC") creates a translation table - a mapping dictionary:

# Creates a mapping:
# 'A' → 'T'
# 'T' → 'A'
# 'C' → 'G'
# 'G' → 'C'

# Actually returns a dictionary with Unicode code points:
# {65: 84, 84: 65, 67: 71, 71: 67}
# ord('A')=65 maps to ord('T')=84
# ord('T')=84 maps to ord('A')=65
# ord('C')=67 maps to ord('G')=71
# ord('G')=71 maps to ord('C')=67

# .translate() replaces each character according to the translation table:
# 'ATTGC'.translate(translation_table) / 'ATTGC'.translate(str.maketrans("ATCG", "TAGC"))

# Process each character:
# 'A' → looks up 65 in table → gets 84 → 'T'
# 'T' → looks up 84 in table → gets 65 → 'A'
# 'T' → looks up 84 in table → gets 65 → 'A'
# 'G' → looks up 71 in table → gets 67 → 'C'
# 'C' → looks up 67 in table → gets 71 → 'G'

# Result: 'TAACG'

# Why translate() is powerful
# str.maketrans() takes 3 forms:
# Form 1: Two strings (character-to-character mapping)
# str.maketrans("abc", "xyz")  # a→x, b→y, c→z

# Form 2: Dictionary
# str.maketrans({'a': 'x', 'b': 'y', 'c': 'z'})

# Form 3: Two strings + delete string
# str.maketrans("abc", "xyz", "123")  # map abc→xyz, delete 1,2,3

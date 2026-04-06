# In this DNA sequence, which is the letter that first occurs 4 times in a
# row?
#
# AAACTTTGGGCCAACCGGGAGGGTTTGCATTTAAATTTGGACCGCCAAACCTGGAAAGGGCCGATTTGGCCCTTAGGTAAATTGCCGGTTTCCCTCCTTTAATTCCGGTGGCCTTGGGGATTCAACCCAAGGACCCAAGGGATTTGCCAATTTCCAGGAAACCCAAACCCAAAGGAAATTTAAATTTCATTTCCCTTTAAACTTAAAATTGTAA

dna = "AAACTTTGGGCCAACCGGGAGGGTTTGCATTTAAATTTGGACCGCCAAACCTGGAAAGGGCCGATTTGGCCCTTAGGTAAATTGCCGGTTTCCCTCCTTTAATTCCGGTGGCCTTGGGGATTCAACCCAAGGACCCAAGGGATTTGCCAATTTCCAGGAAACCCAAACCCAAAGGAAATTTAAATTTCATTTCCCTTTAAACTTAAAATTGTAA"

# letter = ''

# for char in dna:
#     if letter == '':
#         letter += char
#     elif char == letter[0]:
#         letter += char
#         if len(letter) == 4:
#             print(
#                 f'{letter[0]} is the first letter that occurs 4 times in a row')
#             break
#     elif char != letter[0]:
#         letter = ''
#         letter += char


# Alternative solution using while loop

i = 0
found_four = False
while not found_four:
    if dna[i:i+4] == "AAAA" or dna[i:i+4] == "CCCC" or dna[i:i+4] == "GGGG" or dna[i:i+4] == "TTTT":
        found_four = True
    i += 1
print(dna[i])

# There's also AAAA in there, but the GGGG substring comes earlier.

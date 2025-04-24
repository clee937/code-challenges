
 #CodeWars Challenge: [Remove First and Last Character]
 #Link: [https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python]
 #Difficulty: [8 Kyu]

# Instructions

# Create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry about strings with less than two characters.

# for loop
def remove_char(s):
    new_word = ''
    for i in range(1, len(s)-1):
            new_word += s[i]
    return new_word

# string slicing:
# def remove_char(s):
#     return s[1:-1]




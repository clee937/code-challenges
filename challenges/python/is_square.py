# CodeWars Challenge: [You're a Square]
# Link: [https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python]
# Difficulty: [7 Kyu]

# Instructions
# Given an integral number, determine if it's a square number:

# In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. The tests will always use some integral number, so don't worry about that in dynamic typed languages.

# Examples
# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false

from math import sqrt

def is_square(n):    
    return n > -1 and sqrt(n).is_integer()

# def is_square(n):    
#     return n > -1 and sqrt(n) % 1 == 0

# def is_square(n):
#     return n >= 0 and int(n**0.5)**2 == n

print(is_square(-1))
print(is_square(0))
print(is_square(3))
print(is_square(4))
print(is_square(25))
print(is_square(26))

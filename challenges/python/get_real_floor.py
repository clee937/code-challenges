# CodeWars Challenge: [What's the real floor?]
# Link: [https://www.codewars.com/kata/574b3b1599d8f897470018f6/train/python]
# Difficulty: [8 Kyu]

# Instructions
# Write a function that given a floor in the american system returns the floor in the european system. With the 1st floor being replaced by the ground floor and the 13th floor being removed, the numbers move down to take their place. In case of above 13, they move down by two because there are two omitted numbers below them. Basements (negatives) stay the same as the universal level.

# Examples
# 1  =>  0 
# 0  =>  0
# 5  =>  4
# 15  =>  13
# -3  =>  -3

def get_real_floor(floor):
    if floor < 1: return floor
    if floor < 13: return floor - 1
    if floor > 13: return floor - 2
    
def get_real_floor(floor):
    return floor if floor < 1 else floor - 1 if floor < 13 else floor - 2

def get_real_floor(n):
    if n < 1:
        return n
    elif n < 13:
        return n - 1
    else:
        return n - 2
    
print(get_real_floor(1))
print(get_real_floor(0))
print(get_real_floor(5))
print(get_real_floor(15))
print(get_real_floor(-3))
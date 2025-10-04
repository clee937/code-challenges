# CodeWars Challenge: [Get the Middle Character]
# Link: [https://www.codewars.com/kata/56747fd5cb988479af000028/train/python]
# Difficulty: [7 Kyu]

# Instructions
# You are going to be given a non-empty string. Your job is to return the middle character(s) of the string. If the string's length is odd, return the middle character. If the string's length is even, return the middle 2 characters.

# Examples
# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"


# Symmetric slicing
def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s


# Example of divmod() function
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]

# q, r = len(s) / 2, len(s) % 2 is faster than divmod()


# Most readable
def get_middle(s):
    length = len(s)
    mid_index = length // 2
    if length % 2 == 0:
        return s[mid_index-1:mid_index+1]
    else:
        return s[mid_index]


def get_middle(s):
    i = len(s) // 2
    return s[i] if len(s) % 2 != 0 else s[i-1:i+1]


# Calculated slicing
def get_middle(s):
    return s[(len(s)-1)//2:len(s)//2+1]


# Recursive approach. How it works -> Base case: If the string has 1 or 2 characters, return it as-is. Else, recursive case: Strip off the first and last character (s[1:-1]) and call the function again.

def get_middle(s):
    return s if len(s) <= 2 else get_middle(s[1:-1])


'''
"testing" → "estin" → "sti" → "t" (length 1, return!)
 7 chars     5 chars   3 chars  1 char

"test" → "es" (length 2, return!)
4 chars   2 chars

"A" → "A" (length 1, return!)
'''

# Pros: Elegant and easy to understand conceptually. Cons: Slower due to function call overhead; More memory - creates intermediate strings.


print(get_middle("test"))  # --> "es"
print(get_middle("testing"))  # --> "t"
print(get_middle("middle"))  # --> "dd"
print(get_middle("A"))  # --> "A"

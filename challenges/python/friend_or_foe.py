# CodeWars Challenge: [Friend or Foe]
# Link: [https://www.codewars.com/kata/55b42574ff091733d900002f/train/python]
# Difficulty: [7 Kyu]

# Instructions
# Make a program that filters a list of strings and returns a list with only your friends' name in it. If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not. Note: keep the original order of the names in the output.

# Examples
# Input = ["Ryan", "Kieran", "Jason", "Yous"]
# Output = ["Ryan", "Yous"]

# Input = ["Peter", "Stephen", "Joe"]
# Output = []

# 1
def showFriends(x):
    return [friend for friend in x if len(friend) == 4 and friend.isalpha()]

# 2
def showFriends(x):
    myFriends = []
    for name in x:
        if len(name) == 4 and name.isalpha():
            myFriends.append(name)
    return myFriends

print(showFriends(["Ryan", "Kieran", "Jason", "Yous", "1234"]))
print(showFriends(["Peter", "Stephen", "Joe", "1425"]))
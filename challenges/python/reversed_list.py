# Instructions

# Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2. The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

# ==========================================

# Steps

# 1. Define a function that has two input parameters for our lists
# 2. Loop through every index in one of the lists from beginning to end
# 3. Within the loop, compare the element in the first list at the current index against the element at the second list’s last index minus the current index. If there was a mismatch, then the lists aren’t reversed and we can return False
# 4. If the loop ended successfully, then we know the lists are reversed and we can return True.

# ===========================================

def reversed_list(lst1, lst2):
    for index in range(len(lst1)):
        if lst2[len(lst2) - 1 - index] != lst1[index]:
            return False
    return True

# Using reversed():

# def reversed_list(lst1, lst2):
#   return lst1 == list(reversed(lst2))


print(reversed_list([1, 2, 3], [3, 2, 1]))  # True
print(reversed_list([1, 5, 3], [3, 2, 1]))  # False

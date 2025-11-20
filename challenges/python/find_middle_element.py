# CodeWars Challenge: [Find the middle element]
# Link: [https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python]
# Difficulty: [7 Kyu]

# Instructions
# Create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements. The input to the function will be an array of three distinct numbers (Haskell: a tuple).

# Examples:
# gimme([2, 3, 1]) => 0
# 2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.
# gimme([5, 10, 14]) => 1
# 10 is the number that fits between 5 and 14 and the index of 10 in the input array is 1.

def gimme(input_array):
    maximum = max(input_array)
    minimum = min(input_array)

    for index, num in enumerate(input_array):
        if num != maximum and num != minimum:
            return index


def gimme(input_array):
    return input_array.index(sorted(input_array)[1])


def gimme(input_array):
    min, mid, max = sorted(input_array)
    return input_array.index(mid)


def gimme(arr):
    return 3 - arr.index(max(arr)) - arr.index(min(arr))


print(gimme([2, 3, 1]))  # --> 0
print(gimme([5, 10, 14]))  # --> 1

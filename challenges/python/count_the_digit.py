# CodeWars Challenge: [Count the digit]
# Link: [https://www.codewars.com/kata/566fc12495810954b1000030/train/python]
# Difficulty: [7 Kyu]

# Instructions
# Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer. Square all numbers k (0 <= k <= n) between 0 and n. Count the numbers of digits d used in the writing of all the k**2. Implement the function taking n and d as parameters and returning this count. Understanding 'n': n = the highest number you square (not the count of numbers)

# Example 1:
# n = 10, d = 1
# the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
# We are using the digit 1 in: 1, 16, 81, 100. The total count is then 4.

# Example 2:
# The function, when given n = 25 and d = 1 as argument, should return 11 since
# the k*k that contain the digit 1 are:
# 1, 16, 81, 100, 121, 144, 169, 196, 361, 441.
# So there are 11 digits 1 for the squares of numbers between 0 and 25.
# Note that 121 has twice the digit 1.

def count_digit(n, d):
    count = 0
    for i in range(n+1):
        squared_num = i**2
        count += str(squared_num).count(str(d))

    return count


def count_digit(n, d):
    count = 0
    for i in range(n+1):
        count += str(i**2).count(str(d))
    return count


def count_digit(n, d):
    return sum(str(i**2).count(str(d)) for i in range(n+1))


# convert d to a string before entering loop to avoid calling str(d) repeatedly
def count_digit(n, d):
    d = str(d)
    return sum(str(i*i).count(d) for i in range(n+1))


# Only makes one call to count once the full list is produced making it faster
def count_digit(n, d):
    return str([n**2 for n in range(n + 1)]).count(str(d))


print(count_digit(10, 1))  # --> 4
print(count_digit(25, 1))  # --> 11
print(count_digit(5750, 0))  # --> 4700
print(count_digit(11011, 2))  # --> 9481

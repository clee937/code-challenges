# Instructions

# Create a function named exponents() that takes two lists as parameters named 'bases' and 'powers'. Return a new list containing every number in bases raised to every number in powers.

# For example, consider the following code:

# exponents([2, 3, 4], [1, 2, 3])

# The result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64].

# ==================================

# 1. Define the function to accept two lists of numbers, bases and powers
# 2. Create a new list that will contain our answers
# 3. Create a loop that iterates through every base in bases
# 4. Within that loop, create another loop that iterates through every power in power
# 5. Within that nested loop, append the result of the current base raised to the current power.
# 6. After all iterations of both loops are complete, return the list of answers

def exponents(bases, powers):
  answers = []
  for base in bases:
    for power in powers:
      answers.append(base ** power)
  return answers


print(exponents([2, 3, 4], [1, 2, 3]))
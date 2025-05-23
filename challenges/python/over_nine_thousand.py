# Instructions

# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter. The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.

# =====================================

# Steps

# 1. Define the function to accept a list of numbers
# 2. Create a variable to keep track of our sum
# 3. Iterate through every element in our list of numbers
# 4. Within the loop, add the current number we are looking at to our sum
# 5. Still within the loop, check if the sum is greater than 9000. If it is, end the loop
# 6. Return the value of the sum when we ended our loop

def over_nine_thousand(lst):
	sum = 0
	for number in lst:
		sum += number
		if(sum > 9000):
			break
	return sum

print(over_nine_thousand([8000, 900, 120, 5000]))
print(over_nine_thousand([]))
print(over_nine_thousand([8000, 900]))
print(over_nine_thousand([8000]))
print(over_nine_thousand([900, 120, 5000, 1000, 2000, 3000]))
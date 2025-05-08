# CodeWars Challenge: [Binary Addition]
# Link: [https://www.codewars.com/kata/551f37452ff852b7bd000139/train/python]
# Difficulty: [7 Kyu]

# Instructions
# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition. The binary number returned should be a string.

# Examples:
# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

def add_binary(a,b):
	sum = a + b
	value = 1
	
	place_values_list = [1]
	binary_string = ''

	while value * 2 <= sum:
		place_values_list.append(value * 2)
		value *= 2
	
	for number in place_values_list[::-1]:
		print(binary_string)
		if number <= sum:
			binary_string += "1"
			sum -= number
		else:
			binary_string += "0"

	return binary_string or "0"

# Create the result in a list first and then convert to a string. More efficient/performant than adding to a string inside a loop.
def add_binary(a,b):
	sum = a + b
	value = 1
	
	place_values_list = [1]
	binary_list = []

	while value * 2 <= sum:
		place_values_list.append(value * 2)
		value *= 2
	
	for number in place_values_list[::-1]:
		if number <= sum:
			binary_list.append("1")
			sum -= number
		else:
			binary_list.append("0")

	return ''.join(binary_list)


# :b is a format specifier that tells Python to display the default string number in binary
def add_binary(a, b):
    return f"{a + b:b}"

# bin() returns the binary version of an integer. [2:] slicing to remove the default '0b' added to the start.
def add_binary(a, b):
    return bin(a+b)[2:]
	
# CodeWars Challenge: [Testing 1-2-3]
# Link: [https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python]
# Difficulty: [7 Kyu]

# Instructions
# Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering. Write a function which takes a list of strings and returns each line prepended by the correct number. The numbering starts at 1. The format is n: string. Notice the colon and space in between.

# Examples: (Input --> Output)
# [] --> []
# ["a", "b", "c"] --> ["1: a", "2: b", "3: c"]

def number(lines):
	# Check if it's a list
	if not isinstance(lines, list):
		raise TypeError(f"Expected list, got {type(lines).__name__}")
	
	# Check if all elements are strings
	if not all(isinstance(item, str) for item in lines):
		raise TypeError("All elements must be strings")
	
	return [f"{i}: {e}" for i, e in enumerate(lines, 1)]

# def number(lines):
# 	line_numbers = []
# 	for index, element in enumerate(lines, start=1):
# 		line_numbers.append(f"{index}: {element}")
# 	return line_numbers

# def number(lines):
# 	line_numbers = []
# 	for i in range(len(lines)):
# 		line_numbers.append(f"{i+1}: {lines[i]}")
# 	return line_numbers

# def number(lines):
# 	line_numbers = []
# 	count = 1
# 	line_to_add = "" 
# 	for line in lines:
# 		line_to_add = f"{count}: {line}"
# 		line_numbers.append(line_to_add)
# 		count+=1
# 	return line_numbers

# print(number(['a', 'b']))
# print(number(['a', 'b', 'c', 'd']))
# print(number([]))
# print(number(["", "", "", ""]))
# print(number(["a", 2, 45, True]))
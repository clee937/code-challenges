# CodeWars Challenge: [Spin Words]
# Link: [https://www.codewars.com/kata/5264d2b162488dc400000001/train/python]
# Difficulty: [6 Kyu]

# Instructions
# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples
# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test"        --> "This is a test" 
# "This is another test" --> "This is rehtona test"

def spin_words(string):
	if not isinstance(string, str):
		raise TypeError(f"Expected str, got {type(string).__name__}")
	
	if not string:
		raise ValueError("Input cannot be None")
	
	words = string.split()
	processed_words = []
	for word in words:
		word_to_add = word
		if len(word) >= 5:
			word_to_add = word[::-1]
		processed_words.append(word_to_add)
	return ' '.join(processed_words)

# def spin_words(string):
# 	return ' '.join(word if len(word) <5 else word[::-1] for word in string.split())


# print(spin_words('Hey fellow warriors')) # --> "Hey wollef sroirraw"
# print(spin_words('This is a test')) # --> "This is a test"
# print(spin_words('This is another test')) # --> "This is rehtona test"
# print(spin_words(""))

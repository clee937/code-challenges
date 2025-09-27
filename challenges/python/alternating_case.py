# CodeWars Challenge: [Alternating Case]
# Link: [https://www.codewars.com/kata/56efc695740d30f963000557/train/python]
# Difficulty: [8 Kyu]

# Instructions
# Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. As usual, your function/method should be pure, i.e. it should not mutate the original string.

# Examples
# "hello world".toAlternatingCase() === "HELLO WORLD"
# "HELLO WORLD".toAlternatingCase() === "hello world"
# "hello WORLD".toAlternatingCase() === "HELLO world"
# "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
# "12345".toAlternatingCase()       === "12345"  # Non-alphabetical characters are unaffected
# "1a2b3c4d5e".toAlternatingCase()  === "1A2B3C4D5E"
# "String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"

def alternate_case(string):
	if not isinstance(string, str):
		raise TypeError(f"Expected str, got {type(string).__name__}")
	
	# return ''.join(char.swapcase() for char in string)
	# return ''.join(c.lower() if c.isupper() else c.upper() for c in string)
	
	return string.swapcase()


print(alternate_case("hello world")) # "HELLO WORLD"
print(alternate_case("HELLO WORLD")) # "hello world"
print(alternate_case("hello WORLD")) # "HELLO world"
print(alternate_case("HeLLo WoRLD")) # "hEllO wOrld"
print(alternate_case("12345")) # "12345"
print(alternate_case("1a2b3c4d5e")) # "1A2B3C4D5E"
print(alternate_case("String.prototype.toAlternatingCase")) # "sTRING.PROTOTYPE.TOaLTERNATINGcASE"

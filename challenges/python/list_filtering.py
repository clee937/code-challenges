# CodeWars Challenge: [List Filtering]
# Link: [https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python]
# Difficulty: [7 Kyu]

# Instructions
# Create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Examples
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

# checking type with 'isinstance'. Returns boolean.
def filter_list(list):
    return [element for element in list if isinstance(element, int)]

# checking type with 'type()'. Returns the class type.
def filter_list(list):
    return [element for element in list if type(element) == int]

# using not operator with isinstance()
def filter_list(l):
    return [element for element in l if not isinstance(element, str)]

# using not operator with type()
def filter_list(l):
    return [element for element in l if not type(element) == str]

# for in loop
def filter_list(list):
    new_list = []
    for element in list:
        if isinstance(element, int):
            new_list.append(element)
    return new_list

# for loop with range()
def filter_list(list):
    new_list = []
    for index in range(len(list)):
        if type(list[index]) == int:
            new_list.append(list[index])
    return new_list

print(filter_list([1,2,'a','b']))
print(filter_list([1,'a','b',0,15]))
print(filter_list([1,2,'aasf','1','123',123]))
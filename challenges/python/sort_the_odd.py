# CodeWars Challenge: [Sort the odd]
# Link: [https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python]
# Difficulty: [6 Kyu]

# Instructions
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

# Imperative approach with generator expression
def sort_odd_numbers_in_array(source_array):
    
    # Makes a copy so that the original array is not modified.
    result = source_array.copy()
    # result = source_array[:]
    
    # Get odd numbers and sort them. Generator expression - memory efficient. Only one odd number exists in memory at a time.
    odd_numbers = sorted(num for num in result if num % 2 != 0)
    print(type(odd_numbers))
    
    # Replace odd numbers in order
    odd_index = 0
    for i in range(len(result)):
        if result[i] % 2 != 0:  # If odd
            result[i] = odd_numbers[odd_index]
            odd_index += 1
    
    return result

# Functional approach using list comprehension. Pure function - no side effects.
def sort_odd_numbers_in_array(source_array):
    
	# List comprehension - uses more memory than generator expression. All odd numbers stored in a temporary list first.
    odd_numbers = sorted([num for num in source_array if num % 2 != 0])
	
	# Create iterator
    odd_iter = iter(odd_numbers)
    
    return [next(odd_iter) if num % 2 != 0 else num for num in source_array]

# 3
def sort_odd_numbers_in_array(source_array):
    odds = sorted((x for x in source_array if x%2), reverse=True)
    # Without reverse, you can use .pop(0), but that is linear time operation, as opposed to just pop() which is constant time. pop(0) and reverse take about the same amount of time, but with reverse you only need to do it once, instead of .pop(0) for (potentially) every single element.
    
    return [x if x%2==0 else odds.pop() for x in source_array]


print(sort_odd_numbers_in_array([7, 1])) # --> [1, 7]
print(sort_odd_numbers_in_array([5, 8, 6, 3, 4])) # --> [3, 8, 6, 5, 4]
print(sort_odd_numbers_in_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) # --> [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
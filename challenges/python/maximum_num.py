# Instructions:

# Create a function called max_num() that has three parameters named num1, num2, and num3. The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!".

# ================================

# Steps

# 1. Define a function that has three input parameters, num1, num2, and num3.
# 2. Test if num1 is greater than the other two numbers. If so, return num1.
# 3. Test if num2 is greater than the other two numbers. If so, return num2.
# 4. Test if num3 is greater than the other two numbers. If so, return num3.
# 5. If there is a tie between the two largest numbers, then return "It's a tie!" In the case that none of the parameters are greater than both of the other parameters, then we know that there must have been a tie and the final else statement to return ""It's a tie!" will be reached.

def max_num(num1, num2, num3):
  if (num1 > num2 and num1 > num3):
    return num1
  elif (num2 > num1 and num2 > num3):
    return num2
  elif (num3 > num2 and num3 > num1):
    return num3
  else:
    return "It's a tie!"
  

print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
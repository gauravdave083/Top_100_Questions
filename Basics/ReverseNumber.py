# Find the Reverse of a Number in Python
# Given an integer input the objective is to reverse the given integer number using loops and slicing. Therefore, we’ll write a program to Find the Reverse of a Number in Python Language.

# Example
# Input : 123
# Output : 321



# Method 1: Using Simple Iteration
num = 1234
temp = num
reverse = 0
while num > 0: 
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10
    
print(reverse)


# Method 2: Using Recursion

def recursum(number,reverse):
  if number==0:
    return reverse
  remainder = int(number%10)
  reverse = (reverse*10)+remainder
  return recursum(int(number/10),reverse)

num = 1234
reverse = 0
print(recursum(num,reverse))
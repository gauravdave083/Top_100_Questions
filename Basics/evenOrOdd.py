# Check Whether a Number is Even or Odd in Python
# Given an integer input num, the objective is to write a code to Check Whether a Number is Even or Odd in Python. To do so we check if the number is divisible by 2 or not, it’s Even if it’s divisible otherwise Odd.

# Example 
# Input : num = 3
# Output : Odd 

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("Given number is Odd")
    
# Bitwise Operator

def isEven(num):
    
  return not num&1

if __name__ == "__main__":
  num = 13
  if isEven(num):
    print('Even')
  else:
    print('Odd')
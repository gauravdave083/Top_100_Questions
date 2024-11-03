# Check Whether a Number is Even or Odd in Python

# Given an integer input the objective is to write a Python code to Check Whether a Number is Even or Odd. To do so the main idea is to divide the number by 2 and check if it’s divisible or not. It’s an Even number is it’s perfectly divisible by 2 or an Odd number otherwise.


# 1. Brute Force Method

num = int(input("Enter the number: "))

if num % 2 == 0:
     print("Even")
else:
     print("Odd")


# Method 2 : Using Ternary Operator

num = int(input("Enter the number: "))
print("Even" if num % 2 == 0 else "odd")


# Method 3 : Using Bitwise Operator

def isEven(num):
     return not num&1

if __name__ == "__main__":
     num = 13
     if isEven(num):
          print('Even')
     else:
          print('Odd')

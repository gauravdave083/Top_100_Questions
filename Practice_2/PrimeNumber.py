# Check Whether a Number is a Prime or Not in Python
# Given an integer input the objective is to write a program to Check Whether a Number is a Prime or Not in Python Language.

# Example
# Input : 11
# Output : 11 is a Prime

num = 11
flag = 0

for i in range(2, num):
     if num%i==0:
          flag = 1
          break
if flag == 1:
     print("Not Prime")
else:
     print("Prime")




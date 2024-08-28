# Check Whether or Not the Number is a Palindrome in Python
# Given an integer number as an input, the objective is to check Whether or not the number is a palindrome. Therefore, we write a code to Check Whether or Not the Number is a Palindrome in Python Language.

# Example
# Input : 1221
# Output : Palindrome

num = 1221
temp = num
reverse = 0

while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
    
if num ==  reverse:
    print("Palindrome")
else:
    print("Nahi hai")
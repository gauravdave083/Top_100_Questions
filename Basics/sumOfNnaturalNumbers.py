# Find the Sum of N Natural Numbers in Python
# Given an integer input number, the objective is to sum all the numbers that lay from 1 to the integer input number and print the sum. In order to do so we usually use iteration to sum all the numbers until the input variable number.

# Example
# Input : number = 5
# Output : 15
# Explanation : 1 + 2 + 3 + 4 + 5 = 15

number,sum = 6,0

for i in range(number+1):
    sum+=i
print(sum)
    
    
# from recursion

def recursum(number):
    if number == 0:
        return number
    return number + recursum(number-1)

number, sum = 6,0
print(recursum(number))
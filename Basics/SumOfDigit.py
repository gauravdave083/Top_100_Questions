# Find the sum of the Digits of a Number in Python
# Given an input the objective to find the Sum of Digits of a Number in Python. To do so we’ll first extract the last element of the number and then keep shortening the number itself.

# Example
# Input : number = 123
# Output : 6



# Method 0: Using String Character Extraction

num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)

# Method 2: Using Recursion I

num, sum = 12345, 0


def findSum(num, sum):
    if num == 0:
        return sum

    digit = int(num % 10)
    sum += digit
    return findSum(num / 10, sum)


print(findSum(num, sum))


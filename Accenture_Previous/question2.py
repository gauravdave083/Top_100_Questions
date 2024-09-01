# You are required to implement the following Function def LargeSmallSum(arr). 

# The function accepts an integers arr of size ’length’ as its arguments you are required to return the sum of second largest largest element from the even positions and second smallest from the odd position of given ‘arr’.

# Assumption:

# All array elements are unique
# Treat the 0th position a seven

# Return 0 if array is empty
# Return 0, if array length is 3 or less than 3
# Example:-

# Input

# arr:3 2 1 7 5 4

# Output

# 7

# Explanation

# Second largest among even position elements(1 3 5) is 3
# Second largest among odd position element is 4
# Thus output is 3+4 = 7
# Sample Input

# arr:1 8 0 2 3 5 6

# Sample Output

# 8

length = int(input("enter the array: "))
arr = list(map(int, input().split()))
even_arr = []
odd_arr = []

for i in range(length):
    if i % 2 == 0:
        even_arr.append(arr[i])
    else:
        odd_arr.append(arr[i])

even_arr = sorted(even_arr)
odd_arr = sorted(odd_arr)

print(even_arr[len(even_arr)-2] + odd_arr[len(odd_arr)-2])
# Write the program to find the second smallest element in an array using python programming language. We will discuss various method to find the second smallest element of the given array.


# Method 1 : Using two loops
# Method 2 : Using one loop
# Method 3 : Using sort() function.



# Method 1


# float('inf') represents positive infinity in Python. It is a special value provided by the float type, used in cases where you need to represent a value that is larger than any finite number. It is particularly useful in algorithms that need to initialize a variable to a very large value, such as finding the minimum or maximum in a list.

import math

arr = [10, 13, 17, 11, 34, 21]
first = math.inf
second = math.inf

for i in range(0, len(arr)):
   if arr[i] < first:
     first = arr[i]

for i in range(0, len(arr)):
   if arr[i] != first and arr[i] < second:
     second = arr[i]

print(second)



# Method 2

arr = [10, 13, 17, 11, 34, 21]

if len(arr) < 2:
    print("Array must have at least two elements.")
else:
    first = arr[0]
    second = None 

    for i in range(1, len(arr)):
        if arr[i] < first:
            # Update second before first
            second = first
            first = arr[i]
        elif arr[i] != first and (second is None or arr[i] < second):
            # Update second if current element is greater than first but less than second
            second = arr[i]

    if second is None:
        print("Array does not have a second smallest element.")
    else:
        print(second)


# Method 3

import math
arr = [10, 13, 17, 11, 34, 21]
arr.sort()
print(arr[1])
# Second Smallest Element in an array using Python


# Here, in this page we will discuss the program to find the second smallest element in an array using python programming language. We will discuss various method to find the second smallest element of the given array.



# Method 1 : Using two loops

arr = [10, 13, 17, 11, 34, 21]
first = arr[0]
second = arr[0]

for i in range(0, len(arr)):
    if arr[i] < first:
        first = arr[i]

for i in range(0, len(arr)):
    if arr[i] != first and arr[i] < second:
        second = arr[i]

print(second)

# Method 2 : Using sort() function. 

arr = [2, 44, 33, 22, 65, 78, 99, 3, 6, 8]

arr.sort()

print(arr[1])
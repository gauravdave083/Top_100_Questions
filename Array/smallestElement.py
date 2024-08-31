# Find smallest element in an array using Python

# In this section we will learn how to find smallest element in an array using python programming language which is the scripting language. If we want to find smallest element from the array enter by the user so we have to compare one element to other until we get the desired element and print it.



# Method 1: Using Iteration

arr = [10, 89, 9, 56, 4, 80, 8]
min = arr[0]

for i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]

print(min)

# Method 2: Using Sorting

arr = [10, 89, 9, 56, 4, 80, 8]
arr.sort()

print(arr[0])

# Method 3: Using min() function

arr = [10, 89, 9, 56, 4, 80, 8]
print (min(arr))
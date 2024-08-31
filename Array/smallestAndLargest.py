# Smallest and Largest Element in an array using Python
 

# Here, in this page we will discuss the program to find the smallest and largest element in an array using python programming language. We will discuss different algorithms to find the smallest and largest element of the given input array.


# Method 1 : Using Iteration.

arr = [10, 89, 9, 56, 4, 80, 8]
min = arr[0]
max = arr[0]

for i in range(len(arr)):
    if arr[i] < min:
        min = arr[i]
    if arr[i] > max:
        max = arr[i]

print(min)
print(max)



# Method 2 : Using Sort() function.
arr = [10, 89, 9, 56, 4, 80, 8]
arr.sort()

print(arr[0])
print(arr[-1])


# Method 3 : Using max() and min() function
arr = [10, 89, 9, 56, 4, 80, 8]

print (min(arr))
print (max(arr))
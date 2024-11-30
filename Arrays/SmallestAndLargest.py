# Write the program to find the smallest and largest element in an array using python programming language. We will discuss different algorithms to find the smallest and largest element of the given input array.

# Method 1 : Using Iteration.
# Method 2 : Using Sort() function.
# Method 3 : Using max() and min() function


# Method 1

arr = [10, 89, 9, 56, 4, 80, 8]
mini = arr[0]
maxi = arr[0]

for i in range(len(arr)):
  if arr[i] < mini: 
    mini = arr[i] 
  
  if arr[i] > maxi: 
    maxi = arr[i]

print (mini)
print (maxi)


# Method 2

arr = [10, 89, 9, 56, 4, 80, 8]
arr.sort()

print (arr[0])
print (arr[-1])



# Method 3

arr = [10, 89, 9, 56, 4, 80, 8]

print (min(arr))
print (max(arr))
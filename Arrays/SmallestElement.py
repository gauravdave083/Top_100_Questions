# Write a code to find smallest element in an array using python programming language which is the scripting language. If we want to find smallest element from the array enter by the user so we have to compare one element to other until we get the desired element and print it.

# Method 1 : Using Iteration
# Method 2 : Using sorting
# Method 3 : Using min() function



# Method 1

arr = [10, 89, 9, 56, 4, 80, 8]
min_element = arr[0]

for i in range(len(arr)):
     if arr[i] < min_element:
          min-element = arr[i]

print(min_element)

# Method 2

arr = [10, 89, 9, 56, 4, 80, 8]
arr.sort()

print(arr[0])

# Method 3

arr = [10, 89, 9, 56, 4, 80, 8]
print(min(arr))
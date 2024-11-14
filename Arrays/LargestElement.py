#  Write the program to find the largest element in an array using python we are given with an array elements and we need to print the largest among the given elements. 

# Method 1 : Using Iteration
# Method 2 : Using max() function
# Method 3 : Using sort() function.



# Method 1

a = [10, 89, 9, 56, 4, 80, 8]

max_element = a[0]

for i in range(len(a)):
     if a[i] > max_element:
          max_element = a[i]

print(max_element)


# Method - 2

a = [10, 89, 9, 56, 4, 80, 8]
a.sort()

print(a[-1])

# Method - 3

arr = [10, 89, 9, 56, 4, 80, 8]
print (max(arr))
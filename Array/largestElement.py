# Largest Element in an array using python

# Here, in this page we will discuss the program to find the largest element in an array using python we are given with an array elements and we need to print the largest among the given elements. We discuss different methods to find the largest element using python programing language.



# Method 1 : Using Iteration

a = [10, 89, 9, 56, 4, 80, 8]

max_element = a[0]

for i in range(len(a)):
    if a[i] > max_element:
        max_element = a[i]

print(max_element)

# Method 2 : Using sort() function.

a = [10, 89, 9, 56, 4, 80, 8]
a.sort()

print (a[-1])

# Method 3 : Using max() function

arr = [10, 89, 9, 56, 4, 80, 8]
print (max(arr))
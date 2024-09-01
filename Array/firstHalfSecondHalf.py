# Sort First half in Ascending and Second half in descending order in Python

# Here, in this page we will discuss the program to sort first half in ascending and second half in descending order in python programming language. We are given with an array and need to print the array in desired sorting way i.e, first half in increasing order and second half in descending order.

def printOrder(arr, n):
    
    arr.sort()
    
    for i in range(n/2):
        print(arr[i])
        
    for j in range(n-1, n //2 -1, -1):
        print(arr[j])
        
arr = [5, 4, 6, 2, 1, 3, 8, -1]
n = len(arr)
printOrder(arr, n)
# Sum of Elements in an array using Python

# Here, in this page we will discuss the program to find the sum of elements in an array using Python programming language. We are given with an array and need to print the sum of its element. In this page we will discuss different ways to find the sum.



# Method 1 : Using Iteration

arr = [10, 89, 9, 56, 4, 80, 8]
sum = 0

for i in range(len(arr)):
    sum = sum + arr[i]

print(sum)

# Method 2 : Using recursion

def getSum(arr, n):
    if(n == 0):
        return 0
    return arr[n-1] + getSum(arr, n-1)

arr = [10, 20, 30, 40]
print(getSum(arr, len(arr)))

# Method 3 : Using inbuilt Function

arr = [10, 20, 30, 40]
print(sum(arr))
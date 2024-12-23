# Write the program to reverse an array using python programming language. We will discuss different approaches to reverse the array in this page and compare the complexity of different approaches.

# Method 1 : Using Swapping
# Method 2 : Using Recursion
# Method 3 : Using Python List slicing



# Method 1

def reverseList(A, start, end):
  while start < end:
    A[start], A[end] = A[end], A[start]
    start += 1
    end -= 1

A = [10, 20, 30, 40, 50]
reverseList(A, 0, 4)
print(A)

# Method 2

def reverseList(A, start, end):
   if start >= end:
      return
   A[start], A[end] = A[end], A[start]
   reverseList(A, start+1, end-1)

A = [10, 20, 30, 40, 50]
reverseList(A, 0, 4)
print(A)


# Method 3

def reverseList(A):
     print( A[::-1])

A = [10, 20, 30, 40, 50]
reverseList(A)
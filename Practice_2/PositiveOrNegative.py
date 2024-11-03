# Question: Write a program to check if a number is positive, negative or zero


# Brute Force Method to check if a number is positive, negative or zero

num = int(input("Enter a number: "))

if num > 0:
     print("Positive Number")
elif num == 0:                                          # Time Complexity : O(1) , as the code will only execute once regardless of the input size.
     print("Zero")
else:
     print("Negative Number")



# Nested If-Else Method to check if a number is positive, negative or zero

num = int(input("Enter a number: "))

if num >= 0:
     if num== 0: 
          print("Zero")
     else:                                             # Time Complexity : O(1) , as the code will only execute once regardless of the input size.
          print("Positive")
else:
     print("Negative")


#  Method 3: Using Ternary Operator


num = 15
print("Positive" if num > 0 else "Negative")
# Find the Greatest of the Three Numbers
# Given three integer inputs the objective is to find the largest among them. Therefore we write a code to Find the Greatest of the Three Numbers in Python.

# Example
# Input : 20 30 10
# Output : 30


# Method 1: Using if-else Statements

num1, num2, num3 = 10, 30, 20

if num1 >= num2 and num2>= num3:
    print(num1)
elif num2 >= num1 and num3 >= num1:
    print(num2)
else:
    print(num3)
    
# Method 2: Using Nested if-else Statements 
    
num1, num2, num3 = 10 , 350 , 550
max = 0
if num1 >= num2:
    if num1 >= num3:
        print(num1)
elif num2 >= num1:
    if num2 >= num3:
        print(num2)
    else :
        print(num3)
        
# Method 3: Using Ternary Operator

num1, num2, num3 = 10 , 30 , 20
max = num1 if num1>num2 else num2
max = num3 if num3>max else max
print(max)
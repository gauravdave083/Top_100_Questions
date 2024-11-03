# Find the Sum of The First N Natural Numbers in Python
# Given an integer input the objective is to write a code to Find the Sum of First N Natural Numbers in C++. To do so we simply keep adding the value of the iter variable using a for loop.

# Example
# Input : num = 8
# Output : 36

# Where first 8 number is 1, 2, 3, 4, 5, 6, 7, 8
# Sum of numbers = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 = 36


# Method 1 : For Loop
num = 8
sum = 0
for i in range(num+1):                                # Single for loop running n times and incrementing or decrementing by a constant: O(n) Here both loops are running n 
     sum=+i                                           # times and performing O(1) operation at each iteration of the loop. Time complexity = n * O(1) = O(n) * O(1) = O(n).
print(sum)





# Method 2 : Using Formula for the Sum of Nth Term

# Formula to Find the Sum of N terms
# Sum = ( Num * ( Num + 1 ) ) / 2

num = 5
print(int(num*(num+1)/2))




# Check if a Year is a Leap Year or Not in Python
# Given an integer input year, the objective of the code is to Check if a Year is a Leap Year or Not in Python Language. To do so  we’ll check if the year input satisfies either of the two conditions of leap year.

# Example
# Input : 2020
# Output : It's a Leap Year.



# Method 1: Using if-else Statements 1

year = 2000

if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")
    
# Method 2: Using if-else Statements 2

year = 2000
if( ((year % 4 == 0) and (year % 100 != 0)) or (year % 400==0) ):
    print("Leap Year")
else:
    print("Not leap Year")
    
# Method 3: Using Ternary Operator

def check_leap(year): 
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) 

year = int(input("Enter a year: ")) 

print(f"{year} is leap year" if check_leap(year) else f"{year} is not leap year")
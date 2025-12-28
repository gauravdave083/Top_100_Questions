# Check if the number is positive or negative
num = int(input("Enter a number: "))

def check_number(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is zero."

result = check_number(num)
print(result)



# Even or Odd
number = int(input("Enter a number: "))

def check_odd_even(number):
    if number%2 == 0:
        return "The number is even"
    else:
        return "The number is odd"

result = check_odd_even(number)
print(result)



# Sum of first n natural numbers
number = int(input("What is the value of n? "))

def sum_natural_numbers(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum

result = sum_natural_numbers(number)
print("The sum of first", number, "natural numbers is:", result)



# Sum of numbers in a given range:


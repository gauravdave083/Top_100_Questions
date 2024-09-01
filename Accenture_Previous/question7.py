# no. of rats = r
# unit = each rat needs 2 unit of Food
# n = no of houses
# arr = [2, 8, 3, 5, 7, 4, 1, 2]

# output = 4

def calculate(r, unit, arr, n):
    if n == 0:
        return -1
    
    total_food_required = r * units
    foodTillNow = 0
    
    for i in range(n):
        foodTillNow += arr[i]
        if foodTillNow >= total_food_required:
            return i + 1

r = int(input("Enter no of rats: "))
units = int(input("Enter the value for units: "))
n = int(input("Number of elements in array: "))
arr = list(map(int, input("List elements with space seperated: ").split()))

print(calculate(r, units, arr, n))
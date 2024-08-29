num = int(input("enter the number: "))
sum = 0

for i in range(num+1):
    sum+=i
    
print(sum)


# RECURSION

def getSum(num):
    if num == 1:
        return 1
    return num + getSum(num - 1)

num = 2
print(getSum(num))
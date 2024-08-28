# Given two integer as Limits, low and high, the objective is to write a code to in Python Find Prime Numbers in a Given Range in Python Language. To do so we’ll use nested loops to check for the Prime while Iterating through the range.
# Example
# Input : low = 2 , high = 10
# Output : 2 3 5 7

low, high = 2, 10
primes = []

for i in range(low, high - 1):
    flag = 0
    
    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue
    
    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break
    
    if flag == 0:
        primes.append(i)
        
print(primes)
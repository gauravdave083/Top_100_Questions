# Frequency of Elements in an Array in Python

# Here, in this page we will discuss the program to count the frequency of elements in an array in python programming language. We are given with an array and need to print each element along its frequency.


def counter(inpu):
    freq= {}
    
    for i in inpu:
        freq[i] = freq.get(i, 0) + 1
        print(i ,freq[i])
    return freq

print(counter([ 1, 2, 3, 4, 5, 5, 2, 3 ]))


# better method

a = [1, 2, 8, 2, 4, 2, 4, 7]
count = {}

for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

for key,value in count.items():
    print(key,' = ', value)
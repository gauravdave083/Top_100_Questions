def findNum(num):
    if num == 1:
        return 'odd'
    elif num == 2:
        return 'even'
    else:
        return findNum(num - 2)

print(findNum(1))
a = 'silent'

alist = list(a)

b = 'listen'

blist = list(b)

alist.sort()
blist.sort()

if alist == blist:
    print("is anagram")
else:
    print('is not anagram')
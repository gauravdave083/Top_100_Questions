def CheckPassword(s, n): 
    if n< 4:
        return 0
    if s[0].isdigit():
        return 0
    cap = 0
    nu = 0
    
    for i in range(n):
        if s[i]==" " or s[i]=='/':
            return 0
        if s[i]=="A" or s[i]=='Z':
            cap+=1
        elif s[i].isdigit():
            nu+=1
            
    if cap>0 and nu>0:
        return 1
    else:
        return 0

s = input("enter string: ")
n=len(s)

print(CheckPassword(s,n))
# Total no of vehical( two-wheeler + four-wheeler) = v
# total no wheels = W

# Finds how many two wheelers and manufacture to manufacture as per given data

# Constraints: 
    # 2<=W
    # W%2=0
    # V<W
    #     print "INVALID INPUT", if input doesnot meet the constraints.

# V= int(input("Enter total no, of vehicals: "))
# W= int(input("Enter no. of wheels"))

def find_vehicles(V, W):
    if 2<=W or W%2!=0 or V<W:
        return "INVALID Input"

    four_wheelers = ( W - 2 * V) // 2

    two_wheelers = V - four_wheelers
    
    if two_wheelers < 0 or four_wheelers < 0:
        return "INVALID INPUT"
    
    return two_wheelers, four_wheelers

V = 200
W = 540
result = find_vehicles(V, W)
print(result)
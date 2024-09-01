# input1 = bag size
# input 2 = common stones
# input 3 = array with same no of input2, list of 3 common stones

def get_unique_stones_to_bring(M,N,common_stones):
    
    mars_weight = list(range(1, M+1))
    
    earth_weight = common_stones
    
    mars_set = set(mars_weight)
    earth_set = set(earth_weight)
    
    unique_mars_weight = list(mars_set - earth_set)
    
    unique_mars_weight.sort()
    
    total_weight = 0
    num_stones_selected = 0
    
    for i in unique_mars_weight:
        if total_weight + i <= M:
            total_weight += i
            num_stones_selected += 1
        else:
            break
        
    return num_stones_selected

input1 = int(input("capacity of bag: "))
input2 = int(input("Number of common stones from earth: "))
input3 = list(map(int, input("List of stones from earth: ").split()))

output = get_unique_stones_to_bring(input1, input2, input3)
print(output)
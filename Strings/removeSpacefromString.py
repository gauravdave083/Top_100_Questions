# Removing spaces from a string
# Here we will write python program, we will Remove spaces from a string words whether the sentence is meaningful or meaningless and we can do this in two different ways:-

# By traversing the string and removing spaces.
# Using the join function.



# METHOD: 1

String = "PrepInsta is fabulous"

#Use join function 
String = "".join(String.split()) 

print("After removing spaces string is :",String)




# METHOD: 2
s="PrepInsta is fabulous"

# Count no. of spaces in a string
t=s.count(" ")

for i in range(t):
    s=s.replace(' ',"")

print("String after removing space: ")
print(s)
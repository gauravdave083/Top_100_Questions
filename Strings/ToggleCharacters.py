# Toggle each character in a string
# The string is a combination of characters, but in programing language like python, a string is an independent datatype that can be treated as character or string both because in python string of length 1 is also a string, not character. In this python program, we will check the type of string available on the basis of their case

String = 'GuDDuBHaiyA'

String1 = str()

for i in String:
    if i.isupper():
        i = i.lower()
        
        String1 = String1 + i
    else:
        i = i.upper()
        String1 = String1 + i
    
print(String + ' after changing ' + String1)
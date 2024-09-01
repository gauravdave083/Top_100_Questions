# Remove all character from a string except alphabets
# In this article we will learn about how to Remove all character from a string except alphabets

# We will do this by checking ASCII values of each character present in the string and remove all character that does not lie in the range of alphabetic ASCII value whether it is an uppercase letter or a lowercase letter.




String1 = "#Justice!For@Chutki123"

String2 = ''

for i in String1:
    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
        String2+=i

print('Alphabets in string are :' + String2)
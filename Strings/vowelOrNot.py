# Checking a Character is a vowel or consonant in Python

# Here, in this section we will discuss the program to check the entered character is a vowel or consonant in python. In Python string is an array representation of Characters python does not have a character data type. A single character is a string of length [1].

# Vowels:- A character is considered as a vowel when it belongs to the set of characters like { ‘A’ , ‘E’ , ‘I’ , ‘O’ , ‘U’ }

def isLowerCase(c):
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'


def isUpperCase(c):
    return c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'

c = 'f'

if not c.isalpha():
    print("Not alphabet")
elif isLowerCase(c) or isUpperCase(c):
    print(c, "is a Vowel")
else: 
    print(c, "is a consonant")
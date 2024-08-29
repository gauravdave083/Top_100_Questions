# Checking whether a Character is Alphabet or Not in Python ?
# Here, we will discuss program to check whether a Character is alphabet or not in python. All characters whether alphabet, digit or special character have ASCII value. Input character from the user will determine if it’s Alphabet, Number or Special character.

ch = str(input("Enter the character: "))

if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
    print("The charater", ch, "is an alphabet")
else:
    print("The character", ch, "is not an Alphabet")
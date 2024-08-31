# Write a program to check whether a string is palindrome or not in python
input_string = 'civic'
rev = input_string[::-1]

if input_string == rev:
    print(rev + " is Palindrome")
else:
    print(rev + " is not Palindrome")
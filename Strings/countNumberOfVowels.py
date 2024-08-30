# Count the number of vowels in a string
# Program to Count the Number of vowels we’re going to check how many vowels are present in a given String . There are five vowels in English vocabulary, they are – ‘a’, ‘e’, ‘i’, ‘o’, ‘u’.

# For Example, in the string prepinsta then in that case then vowesl are 3 (a,e,i)

string = 'ALKJEtgdb'

count = 0

string = string.lower()

for i in string:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count +=1

if count == 0:
    print("No vowel founds")
else:
    print("Total vowels are: " + str(count))
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
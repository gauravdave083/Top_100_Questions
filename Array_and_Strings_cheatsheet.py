

### 1. **Array Operations**

#### 1.1. **Creating an Array**

arr = [1, 2, 3, 4, 5]


#### 1.2. **Accessing Elements**

first_element = arr[0]  # 1
last_element = arr[-1]  # 5


#### 1.3. **Adding Elements**

arr.append(6)  # Adds 6 at the end
arr.insert(2, 99)  # Inserts 99 at index 2

#### 1.4. **Removing Elements**

arr.remove(99)  # Removes the first occurrence of 99
popped_element = arr.pop()  # Removes and returns the last element (6)


#### 1.5. **Sorting the Array**

arr.sort()  # Sorts the array in ascending order
arr.sort(reverse=True)  # Sorts the array in descending order


#### 1.6. **Reversing the Array**

arr.reverse()  # Reverses the elements in the array


#### 1.7. **Slicing the Array**

sub_array = arr[1:4]  # Extracts elements from index 1 to 3


#### 1.8. **Finding the Maximum and Minimum**

max_value = max(arr)  # Maximum element
min_value = min(arr)  # Minimum element

#### 1.9. **Converting Array to String**

arr = [1, 2, 3, 4]
arr_str = ''.join(map(str, arr))  # '1234'


### 2. **String Operations**

#### 2.1. **Creating a String**

s = "Hello, World!"


#### 2.2. **Accessing Characters**

first_char = s[0]  # 'H'
last_char = s[-1]  # '!'


#### 2.3. **Slicing the String**

substring = s[7:12]  # 'World'


#### 2.4. **Concatenating Strings**

s2 = " How are you?"
combined_string = s + s2  # 'Hello, World! How are you?'

#### 2.5. **Finding a Substring**

index_of_world = s.find("World")  # 7


#### 2.6. **Replacing Substrings**

new_s = s.replace("World", "Python")  # 'Hello, Python!'


#### 2.7. **Converting String to Upper/Lower Case**

upper_s = s.upper()  # 'HELLO, WORLD!'
lower_s = s.lower()  # 'hello, world!'


#### 2.8. **Splitting a String into an Array**

words = s.split()  # ['Hello,', 'World!']


#### 2.9. **Joining an Array into a String**

words = ['Python', 'is', 'fun']
joined_str = ' '.join(words)  # 'Python is fun'


#### 2.10. **Converting String to List of Characters**

char_list = list(s)  # ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!']


### 3. **Converting Between Array and String**

#### 3.1. **Array to String**

arr = ['P', 'y', 't', 'h', 'o', 'n']
arr_str = ''.join(arr)  # 'Python'


#### 3.2. **String to Array**

s = "Python"
arr = list(s)  # ['P', 'y', 't', 'h', 'o', 'n']


### 4. **Looping through Arrays and Strings**

#### 4.1. **Looping Through an Array**

for element in arr:
    print(element)


#### 4.2. **Looping Through a String**

for char in s:
    print(char)

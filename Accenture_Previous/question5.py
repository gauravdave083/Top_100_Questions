# You are given a function, Void *ReplaceCharacter(Char str[], int n, char ch1, char ch2);

# The function accepts a string  ‘ str’ of length n and two characters ‘ch1’ and ‘ch2’ as its arguments . Implement the function to modify and return the string ‘ str’ in such a way that all occurrences of ‘ch1’ in original string are replaced by ‘ch2’ and all occurrences of ‘ch2’  in original string are replaced by ‘ch1’.

# Assumption: String Contains only lower-case alphabetical letters.

# Note:

# Return null if string is null.
# If both characters are not present in string or both of them are same , then return the string unchanged.
# Example:

# Input:
# Str: apples
# ch1:a
# ch2:p
# Output:
# Paales
# Explanation:

# ‘A’ in original string is replaced with ‘p’ and ‘p’ in original string is replaced with ‘a’, thus output is paales.

def replace_character(s, ch1, ch2):
    # Check if the string is None
    if s is None:
        return None

    # If both characters are the same or neither character is in the string, return the string unchanged
    if ch1 == ch2 or (ch1 not in s and ch2 not in s):
        return s

    # Create a translation table
    translation_table = str.maketrans({ch1: ch2, ch2: ch1})

    # Use the translation table to replace characters
    return s.translate(translation_table)

# Example usage
s = "apples"
ch1 = 'a'
ch2 = 'p'
result = replace_character(s, ch1, ch2)
print("Output:", result)

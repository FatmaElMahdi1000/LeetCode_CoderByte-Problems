"""💬 Problem Description:
Vowel Count
Write a function that takes a string as input and counts how many vowels (a, e, i, o, u) are present in the string. The string may include spaces, symbols, and both lowercase and uppercase letters.
"""

def VowelCount(s):
    vowels = "aeiou"
    count = 0

    for char in s.lower():
        if char in vowels:
            count += 1
    return count 


count = VowelCount("I am Fatma ElMahdi!")
print(count)
        
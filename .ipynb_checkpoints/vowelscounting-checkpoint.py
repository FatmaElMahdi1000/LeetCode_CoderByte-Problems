"""Have the function VowelCount(str) take the str string parameter being passed and return the number of vowels the string contains (ie. “All cows eat grass and moo” would return 8). Do not count y as a vowel for this challenge. """



def VowelCount(str):
    
    Vowels = ["a", "e", "i", "o", "u"]
    str = str.lower()
    findings = []
    
    for char in str:
        if char in Vowels:
            findings.append(char)
    count = len(findings)
    return count

result = VowelCount("hello there Iam fatme!")
print(result)

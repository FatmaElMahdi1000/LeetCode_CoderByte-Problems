def Palindrome(strParam):
    
    cleaned = ""
    for char in strParam:
        if char.isalnum(): 
            cleaned = cleaned + char.lower()  # concatenation method .
    Reversed = "".join(reversed(cleaned))
    print(Reversed)
    return cleaned == Reversed 

sentence = Palindrome("race car")

print(sentence)
            
sentence = Palindrome("race car")

print(sentence)


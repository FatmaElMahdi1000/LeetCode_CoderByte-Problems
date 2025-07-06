#return string with each letter and the corresponding count. 

#1giving the index. count 
def LetterCount(strParam):
    result = list(enumerate(strParam))
    return result

result = LetterCount("Hello!")
print(result)


#1
def LetterCount(strParam):
    dictionary = {}
    for char in strParam:
        if char.isalpha(): #checking if we only have letters
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
    return dictionary

result = LetterCount("Helllo!")
print(result)

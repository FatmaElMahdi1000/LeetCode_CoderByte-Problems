""" 
getting word count. not character count
"""

def WordCount(str):
    words = str.split() #split sentence to words 
    words_length = len(words)
    return words_length
    
print(WordCount("Hello, I am Fatma!"))
print("#____Different Solutions____#")
def WordCount(string):

    stringtolist = string.split()
    count = 0
    for word in stringtolist:
        count += 1
    return count 
        

String = WordCount("Hi There!")

    
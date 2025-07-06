""" 
getting word count. not character count
"""

def WordCount(str):
    words = str.split() #split sentence to words 
    words_length = len(words)
    return words_length
    
print(WordCount("Hello, I am Fatma!"))

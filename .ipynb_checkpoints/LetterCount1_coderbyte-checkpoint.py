"""have the function LetterCountI(str) take the str parameter being passed and return the first word with the greatest number of repeated letters. For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's. 

If there are no words with repeating letters return -1. Words will be separated by spaces."""


def LetterCount(sentence):
    words = sentence.split()
    best_word = "-1"
    best_repeat = 0

    for word in words:
        count = {}  # count letters in this word

        for letter in word:
            if letter.isalpha():
                if letter not in count:
                    count[letter] = 1
                else:
                    count[letter] += 1

        # Find the highest repeat in this word
        most_common = 1
        for times in count.values():
            if times > most_common:
                most_common = times

        # If this word has more repeats than any before, save it
        if most_common > best_repeat:
            best_repeat = most_common
            best_word = word

    # If no letter was ever repeated (i.e. best_repeat is still 1), return -1
    if best_repeat == 1:
        return "-1"
    else:
        return best_word

                
                    
    
#!/usr/bin/env python3
import sys
import difflib

def get_meaning(word):
    """Takes word and find all meanings of it and returns the list of all meanings
    :param word: sting for which the meaning will be searched 
    :returns: list of all meanings if found"""

    list_of_meanings = []
    #index                              0      1      2
    #format of the 'dictionary.csv' is: "word","type","meaning" per line
    with open("dictionary.csv") as wordfile:
        for line in wordfile:
            split_line = line.split(",")
            if split_line[0].strip('"') == word:
                list_of_meanings.append(split_line[2])
    return list_of_meanings

def get_set_of_words():
    """Gives set of words from the dictionary source file
    :returns: set of all words from the file"""

    set_of_words = set()
    with open("dictionary.csv") as wordfile:
        for line in wordfile:
            set_of_words.add(line.split(",")[0].strip('"'))
    return set_of_words 
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please specify a word to find the meaning. \nUsage:\n $ python3 eictionary.py word") 
    else:
        meanings = get_meaning(sys.argv[1])
        if not meanings:
            print("Word '{0}' not found, some similar words: ".format(sys.argv[1]))
            for related in difflib.get_close_matches(sys.argv[1], get_set_of_words()):
                print(related)
        else:
            for meaning in meanings:
                print(meaning)

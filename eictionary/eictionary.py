#!/usr/bin/env python3
import sys

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

def get_list_of_words():
    """Gives list of words from the dictionary source file
    :returns: list of all words from the file"""

    list_of_words = []
    with open("dictionary.csv") as wordfile:
        for line in wordfile:
            list_of_words = line.split(",")[0].strip('"')
    return list_of_words        
        
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please specify a word to find the meaning. \nUsage:\n $ python3 eictionary.py word") 
    else:
        for meaning in get_meaning(sys.argv[1]):
            print(meaning)

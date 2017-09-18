#!/usr/bin/env python3

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



if __name__ == "__main__":
    for meaning in get_meaning("Good"):
        print(meaning)

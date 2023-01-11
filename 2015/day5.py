#!/usr/bin/python3

import requests

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}

puzzle_input = requests.get("https://adventofcode.com/2015/day/5/input", cookies=cookie)

inputstring = puzzle_input.text
inputlist = inputstring.split("\n")

verbose = True
nice_strings = 0

def three_or_more_vowels(word):
    vowel_count = 0
    for vowel in word:
        if vowel in 'aeiou':
            vowel_count += 1
    if vowel_count >= 3:
        if verbose:
            print(word, " has 3 or more vowels")
        return True
    print(word, " has ", vowel_count, " vowels")
    return False

def letter_twice_in_row(word):
    last_letter = ''
    for i in word:
        if i == last_letter:
            if verbose:
                print(word," contains: ", last_letter,i)
            return True
        else:
            last_letter = i
    return False
        
def substrings_in_word(word):
    unwanted = ['ab','cd','pq','xy']
    for i in unwanted:
        if i in word:
            return True
    return False
    
for entry in inputlist[:-1]:
    if three_or_more_vowels(entry) == True:
        if letter_twice_in_row(entry) == True:
            if substrings_in_word(entry) == False:
                #print(entry)
                nice_strings += 1

print(len(inputlist))
print(nice_strings)



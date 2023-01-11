#!/usr/bin/python3

import requests

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}

puzzle_input = requests.get("https://adventofcode.com/2015/day/5/input", cookies=cookie)

inputstring = puzzle_input.text
inputlist = inputstring.split("\n")
nice_strings = 0

pair_counter = 0
repeat_container = 0 

def contains_pair(entry):
    # contains a pair of any two letters that appears at least twice in the string without overlapping
    # print(entry[0:0+2])
    # print(entry.count(entry[0:0+2]))
    global pair_counter
    for i in range(len(entry)-2):
        if entry.count(entry[i:i+2])>=2:
            print(entry, "has", entry[i:i+2], "2 or more times")
            pair_counter += 1
            return True
    return False

def contains_repeat(entry):
    # contains at least one letter which repeats with exactly one letter between them
    global repeat_container
    for i in range(len(entry)-2):
        if entry[i] == entry[i+2]:
            print(entry, "has", entry[i], entry[i+2])
            repeat_container += 1
            return True
    return False

    #learning usage of the any() function
    # if any([(entry[i] == entry[i+2]) for i in range(len(entry)-2)]):
    #     print(entry, "has", entry[i], entry[i+2])
    #     return True

for entry in inputlist:
    if contains_pair(entry) and contains_repeat(entry):
        nice_strings += 1

print(nice_strings)




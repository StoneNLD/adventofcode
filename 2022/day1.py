#!/usr/bin/python3

import requests

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}
puzzle_input = requests.get("https://adventofcode.com/2022/day/1/input", cookies=cookie)
inputlist = puzzle_input.text.split("\n")[:-1]

#print(inputlist)

max_callories = 0
carrying_cals = 0
elve_number = 1

for record in inputlist:
    # "" marks a new elve
    if record != "":
        carrying_cals += int(record)
        if carrying_cals > max_callories:
            print("This is elve number:",elve_number)
            max_callories = carrying_cals
    else:
        # continue to next elve
        assert record == ""
        carrying_cals = 0
        elve_number += 1

print(max_callories)
#!/usr/bin/python3

import requests

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}
puzzle_input = requests.get("https://adventofcode.com/2022/day/1/input", cookies=cookie)
inputlist = puzzle_input.text.split("\n")[:-1]

#print(inputlist)

cals_per_elve = []
carrying_cals = 0
elve_number = 1

for record in inputlist:
    # "" marks a new elve
    if record != "":
        carrying_cals += int(record)
    else:
        # continue to next elve
        assert record == ""
        cals_per_elve.append(carrying_cals)
        carrying_cals = 0
        elve_number += 1

print(sum(sorted(cals_per_elve)[-3:]))
#!/usr/bin/python3

import requests

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}
puzzle_input = requests.get("https://adventofcode.com/2022/day/4/input", cookies=cookie)
inputlist = puzzle_input.text.split("\n")[:-1]

#inputlist = ["2-4,6-8","2-3,4-5","5-7,7-9","2-8,3-7","6-6,4-6","2-6,4-8","7-63,13-99"]

overlapping_counter = 0
for item in inputlist:
    first_section, second_section = item.split(",")[0], item.split(",")[1]
    #print("these are the sections:", first_section, second_section)
    start1, end1 = first_section.split("-")[0], first_section.split("-")[1]
    start2, end2 = second_section.split("-")[0], second_section.split("-")[1]
    #print(start1, end1, start2, end2)
    if (int(start1) >= int(start2) and int(end1) <= int(end2)) or (int(start2) >= int(start1) and int(end2) <= int(end1)):
        print(first_section, "overlaps with", second_section)
        overlapping_counter += 1

print("Overlapping counter:",overlapping_counter)

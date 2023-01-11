#!/usr/bin/python3

import requests

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}
puzzle_input = requests.get("https://adventofcode.com/2022/day/4/input", cookies=cookie)
inputlist = puzzle_input.text.split("\n")[:-1]

#inputlist = ["2-4,6-8","2-3,4-5","5-7,7-9","2-8,3-7","6-6,4-6","2-6,4-8","7-63,13-99"]
total_items = len(inputlist)
non_overlapping_counter = 0

for item in inputlist:
    first_section, second_section = item.split(",")[0], item.split(",")[1]
    #print("these are the sections:", first_section, second_section)
    start1, end1 = first_section.split("-")[0], first_section.split("-")[1]
    start2, end2 = second_section.split("-")[0], second_section.split("-")[1]
    #print(start1, end1, start2, end2)
    if (int(end1) < int(start2)) or int(end2) < int(start1): 
        print(first_section, "does not have overlap with", second_section)
        non_overlapping_counter += 1

print("Non overlapping counter:",non_overlapping_counter)
print("Total Overlapping items:", total_items - non_overlapping_counter)

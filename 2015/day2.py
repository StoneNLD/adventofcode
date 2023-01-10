#!/usr/bin/python3

import requests

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}
puzzle_input = requests.get("https://adventofcode.com/2015/day/2/input", cookies=cookie)

# Take dimensions and compute amount of paper per gift
def compute_needs(dimensions):
    l = int(dimensions.split("x")[0])
    w = int(dimensions.split("x")[1])
    h = int(dimensions.split("x")[2])
    dimension_list = [l,w,h]
    # provided in question
    paper_surface = 2*l*w + 2*w*h + 2*h*l
    # smallest side
    paper_extra = min(l*w,w*h,h*l)
    total_paper_per_gift = paper_surface + paper_extra
    # 2 smallest surface sides
    ribbon_surface = (2*sorted(dimension_list)[0]) + 2*(sorted(dimension_list)[1])
    ribbon_bow = int(l*w*h)
    total_ribbon_needed = ribbon_surface + ribbon_bow
    return total_paper_per_gift, total_ribbon_needed

total_paper_needed = 0
total_ribbon_needed = 0

inputstring = puzzle_input.text
inputlist = inputstring.split("\n")

#trim last emptyline from list
for gift in inputlist[:-1]:  
    total_paper_needed += compute_needs(gift)[0]
    total_ribbon_needed += compute_needs(gift)[1]

print(total_paper_needed)
print(total_ribbon_needed)
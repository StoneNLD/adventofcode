#!/usr/bin/python3

import requests

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}
puzzle_input = requests.get("https://adventofcode.com/2015/day/1/input", cookies=cookie)

floor = 0
position= 0

for move in puzzle_input.text:
    if floor < 0:
        break
    if move == "(":
         print("going up 1 floor")
         floor += 1
         print("we are now on floor", floor )
    if move == ")":
        print("going down 1 floor")
        floor -= 1
        print("we are now on floor", floor )
    position += 1
        
print("We are on floor: ", floor)
print("position we entered basement: ", position)






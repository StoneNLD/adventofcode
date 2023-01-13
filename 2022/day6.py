#!/usr/bin/python3

import requests

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}
puzzle_input = requests.get("https://adventofcode.com/2022/day/5/input", cookies=cookie)
inputlist = puzzle_input.text.split("\n")[:-1]

#print(inputlist)
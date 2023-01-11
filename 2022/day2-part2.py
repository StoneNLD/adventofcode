#!/usr/bin/python3

import requests

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}
puzzle_input = requests.get("https://adventofcode.com/2022/day/2/input", cookies=cookie)
inputlist = puzzle_input.text.split("\n")[:-1]

print(inputlist)

total_points = 0
def calculate_points(entry):
    global total_points
    if entry.split()[0] == "A":
        if entry.split()[1] == "X":
            # 0 for lose, 3 for shape
            total_points += 3
        elif entry.split()[1] == "Y":
            # 3 for draw, 1 for shape
            total_points += 4
        elif entry.split()[1] == "Z":
            # 6 for win, 2 for shape
            total_points += 8
    elif entry.split()[0] == "B":
        if entry.split()[1] == "X":
            # 0 for loss, 1 for shape
            total_points += 1
        elif entry.split()[1] == "Y":
            # 3 for draw, 2 for shape
            total_points += 5
        elif entry.split()[1] == "Z":
            # 6 for win, 3 for shape
            total_points += 9
    elif entry.split()[0] == "C":
        if entry.split()[1] == "X":
            # 0 for loss, 2 for shape
            total_points += 2
        elif entry.split()[1] == "Y":
            # 3 for draw, 3 for shape
            total_points += 6
        elif entry.split()[1] == "Z":
            # 6 for draw, 1 for shape
            total_points += 7

for entry in inputlist:
    calculate_points(entry)

print(total_points)
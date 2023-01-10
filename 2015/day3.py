#!/usr/bin/python3

import requests

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}
puzzle_input = requests.get("https://adventofcode.com/2015/day/3/input", cookies=cookie)

#print(puzzle_input.text)

x = 0
y = 0

x1 = 0
y1 = 0
# convert to usable input
inputstring = puzzle_input.text
inputlist = list(inputstring)


santa_input = inputlist[::2]
robosanta_input = inputlist[1::2]

def step_santa(direction):
    global x, y
    if direction == "^":
        y += 1
    elif direction == "v":
        y -= 1
    elif direction == "<":
        x -= 1
    elif direction == ">":
        x += 1
    return x, y

def step_robosanta(direction):
    global x1, y1
    if direction == "^":
        y1 += 1
    elif direction == "v":
        y1 -= 1
    elif direction == "<":
        x1 -= 1
    elif direction == ">":
        x1 += 1
    return x1, y1

visited_coordinates = []

for direction in santa_input:
     print("Santa Stepping in direction", direction)
     step_santa(direction)
     print("Santa is at x, y coord: ", x, y)
     # append uniq (unvisited) coord to list
     if [x,y] not in visited_coordinates:
       visited_coordinates.append([x,y])

for direction in robosanta_input:
     print("Robosanta Stepping in direction", direction)
     step_robosanta(direction)
     print("Robosanta is at x, y coord: ", x1, y1)
     # append uniq (unvisited) coord to list
     if [x1,y1] not in visited_coordinates:
       visited_coordinates.append([x1,y1])

# # print(visited_coordinates)
print(len(visited_coordinates))



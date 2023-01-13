#!/usr/bin/python3

import requests
import time

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}
puzzle_input = requests.get("https://adventofcode.com/2022/day/5/input", cookies=cookie)
inputlist = puzzle_input.text.split("\n")[:-1]

inputlist = [x for x in inputlist if x.startswith('move')]
#inputlist = ["move 1 from 2 to 1", "move 3 from 1 to 3", "move 2 from 2 to 1", "move 1 from 1 to 2"]
#print(inputlist)

verbose = False
visualise = False
stack = [["B", "W", "N"], ["L", "Z", "S", "P", "T", "D", "M", "B"], ["Q", "H", "Z", "W", "R"],["W", "D", "V", "J", "Z", "R"],
["S", "H", "M", "B"],["L", "G", "N", "J", "H", "V", "P", "B"], ["J", "Q", "Z", "F", "H", "D", "L", "S"], 
["W", "S", "F", "J", "G", "Q", "B"], ["Z", "W", "M", "S", "C", "D", "J"] ]

def visualise_stack():
    print("*"*50)
    for i in stack:
        print("stack",stack.index(i) + 1, i[:len(i)])
    time.sleep(1) 

def move(entry):
    amount = entry.split()[1]
    if verbose:
        print("Moving", amount, "containers")
    source_stack = entry.split()[3]
    if verbose:
        print("Taking containers from", source_stack)
    dest_stack = entry.split()[5]
    if verbose:
        print("Adding containers to", dest_stack)
    for times in range(int(amount)):
        item_to_move = stack[int(source_stack) -1][-1]
        if verbose:
            print("Item to move:", item_to_move)
        stack[int(source_stack) -1].pop()
        stack[int(dest_stack) -1].append(item_to_move)

for entry in inputlist:
    move(entry)
    if visualise:
        visualise_stack()

print("Top containers are:", stack[0][-1] + stack[1][-1] + stack[2][-1] + stack[3][-1] + 
stack[4][-1] + stack[5][-1] + stack[6][-1] + stack[7][-1] + stack[8][-1])


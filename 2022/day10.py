#!/usr/bin/python3

import requests

def grab_input():
    sessionid = input("sessionid from cookie: ")
    cookie = {'session': sessionid}
    puzzle_input = requests.get("https://adventofcode.com/2022/day/10/input", cookies=cookie)
    inputlist = puzzle_input.text.split("\n")[:-1]
    return inputlist

inputlist = grab_input()
# print(inputlist)

testinput = ["noop", "addx 3", "addx -5"]
testinput2 = [
"addx 15",
"addx -11",
"addx 6",
"addx -3",
"addx 5",
"addx -1",
"addx -8",
"addx 13",
"addx 4",
"noop"
]

def cycles_to_steps(inputlist, cycles):
    counter = 0
    amount_steps = 0
    for step in inputlist:   
        if counter >= cycles:
            break
        if step.startswith("noop"):
            counter += 1
            amount_steps += 1
        else:
            if step.startswith("addx"):
                counter += 2
                amount_steps += 1 
    return amount_steps

def signal_strength(inputlist, cycles):
    steps = cycles_to_steps(inputlist, cycles)
    X = 1
    for i in inputlist[:steps -1]:
        if i == "noop":
            continue
        else:
            assert i.startswith("addx")
            X += int(i.split()[1])
    return X * cycles

def part1():
    value = 0
    for i in range(20,260,40):
        value += signal_strength(inputlist,i)
    print("Value of X is:", value) 

part1()


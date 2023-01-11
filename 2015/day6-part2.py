#!/usr/bin/python3

import requests
import numpy as np

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}
puzzle_input = requests.get("https://adventofcode.com/2015/day/6/input", cookies=cookie)
inputlist = puzzle_input.text.split("\n")[:-1]

verbose = True
grid = np.zeros((1000, 1000), 'int32')

#print(inputlist)

for line in inputlist:
    line = line.split()

    # Turn on/off
    if line[0] == 'turn':
        x1, y1 = line[2].split(',')
        x2, y2 = line[4].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

        if line[1] == 'on':
            grid[x1:x2+1, y1:y2+1] += 1

        else:
            assert line[1] == 'off'
            grid[x1:x2+1, y1:y2+1] -= 1
            grid[grid < 0] = 0

    # Toggle
    else:
        assert line[0] == 'toggle'
        x1, y1 = line[1].split(',')
        x2, y2 = line[3].split(',')
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        grid[x1:x2+1, y1:y2+1] += 2

    if verbose:
        print('x1, y1:', x1, y1)
        print('x2, y2:', x2, y2)

print(np.sum(grid))
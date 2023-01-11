#!/usr/bin/python3

import requests

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}
puzzle_input = requests.get("https://adventofcode.com/2022/day/3/input", cookies=cookie)
inputlist = puzzle_input.text.split("\n")[:-1]

#print(inputlist)

items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
itemslist = list(items)
misplaced_list = []

for backpack in inputlist:
    for item in backpack[:len(backpack)//2]:
        if item in backpack[len(backpack)//2:]:
            misplaced_list.append(item)
            break
print(misplaced_list)

total_priority = 0
for item in misplaced_list:
    print("adding", item, "with priority of", (itemslist.index(item) + 1))
    total_priority += (itemslist.index(item) + 1)
    print("Total priority of all items is now:", total_priority)

print(total_priority)


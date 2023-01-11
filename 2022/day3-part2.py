#!/usr/bin/python3

import requests

sessionid = input("sessionid from cookie: ")
cookie = {'session': sessionid}
puzzle_input = requests.get("https://adventofcode.com/2022/day/3/input", cookies=cookie)
inputlist = puzzle_input.text.split("\n")[:-1]

#print(inputlist)
#inputlist = ["vJrwpWtwJgWrhcsFMMfFFhFp","jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg","wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn","ttgJtRGJQctTZtZT","CrZsJsPPZsGzwwsLwLmpwMDw"]

def divide_chunks(input, chunksize):
    for i in range(0, len(input), chunksize):
        yield input[i:i + chunksize]

newlist = list(divide_chunks(inputlist, 3))

items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
itemslist = list(items)

total_value = 0 

for chunk in newlist:
    for item in chunk[0]:
            if item in chunk[1] and item in chunk[2]:
                total_value += (itemslist.index(item) + 1)
                break

print(total_value)

# print(total_value)

# items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# itemslist = list(items)
# misplaced_list = []

# for backpack in inputlist:
#     for item in backpack[:len(backpack)//2]:
#         if item in backpack[len(backpack)//2:]:
#             misplaced_list.append(item)
#             break
# print(misplaced_list)

# total_priority = 0
# for item in misplaced_list:
#     print("adding", item, "with priority of", (itemslist.index(item) + 1))
#     total_priority += (itemslist.index(item) + 1)
#     print("Total priority of all items is now:", total_priority)

# print(total_priority)


#print(misplaced_list)
# for item in enumerate(items):
#     print(item)

# backpack = "qwebrtyuiopFGHqJKqLT"
# backpacklist = list(backpack)
# print(backpack[:len(backpack)//2])
# print(backpack[len(backpack)//2:])
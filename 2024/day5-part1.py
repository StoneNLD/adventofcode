#!/usr/bin/python3

import requests

def grab_input():
    sessionid = input("sessionid from cookie: ")
    cookie = {'session': sessionid}
    response = requests.get("https://adventofcode.com/2024/day/5/input", cookies=cookie)
    return response.text.strip().split("\n")

rules_input = [
    (47, 53),
    (97, 13),
    (97, 61),
    (97, 47),
    (75, 29),
    (61, 13),
    (75, 53),
    (29, 13),
    (97, 29),
    (53, 29),
    (61, 53),
    (97, 53),
    (61, 29),
    (47, 13),
    (75, 47),
    (97, 75),
    (47, 61),
    (75, 61),
    (47, 29),
    (75, 13),
    (53, 13)
]

updates_input = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47]
]

test_output_part1 = 143

test_input_part2 = []
test_output_part2 = 9

def is_correct_order(update, rules):
    # Helper function to check if a given update is in the correct order
    for rule in rules:
        x, y = rule
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True

def find_middle_page(update):
    # Helper function to find the middle page number
    update = update.split(',')
    length = len(update)
    middle_index = int((length - 1) // 2)
    return update[middle_index]

def sum_middle_pages(updates, rules):
    # Helper function to sum the middle pages of all valid updates
    valid_updates = []
    for update in updates:
        if is_correct_order(update, rules):
            valid_updates.append(update)

    count = 0    
    for update in valid_updates:
        count += (int(find_middle_page(update)))

    return count

def test_function_part1():
    assert True == True

def test_function_part2():
    assert True == True

def part1(inputlist): 
    separator_index = inputlist.index("")
    rules_part1 = inputlist[:separator_index]
    rules_tuplelist = []
    for i in rules_part1:
        x, y = i.split('|')
        rules_tuplelist.append((x, y))
    updates_part1 = inputlist[separator_index + 1:]
    print(sum_middle_pages(updates_part1, rules_tuplelist))

if __name__ == "__main__":
     inputlist = grab_input()
     part1(inputlist)

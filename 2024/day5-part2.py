#!/usr/bin/python3

import requests

def grab_input():
    sessionid = input("sessionid from cookie: ")
    cookie = {'session': sessionid}
    response = requests.get("https://adventofcode.com/2024/day/5/input", cookies=cookie)
    response = response.text.strip().split("\n")
    updates: list = []
    rules: dict = {}
    for line in response:
        if "|" in line:
            a, b = line.strip().split("|")
            if a not in rules:
                rules[a] = []
            rules[a].append(b)
        else:
            if line.strip():
                updates.append(line.strip().split(","))
    return updates, rules

def correct_order(update: list, fix_wrong=False) -> int:
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            rule = rules.get(update[j], [])
            if update[i] in rule:
                if fix_wrong:
                    update[i], update[j] = update[j], update[i]
                    return correct_order(update, True)
                else:
                    return 0

    return int(update[len(update) // 2])


result_1 = 0
result_2 = 0

updates, rules = grab_input()

for update in updates:
    result_1 += correct_order(update)
    result_2 += correct_order(update, True)

print("Solution 1:", result_1)
print("Solution 2:", result_2 - result_1)
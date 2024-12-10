#!/usr/bin/python3

import requests

def grab_input():
    # sessionid = input("sessionid from cookie: ")
    sessionid = '53616c7465645f5f16478a7c79a602bcfd37c7ccd166fecaeb784d9b005613eb0d0606c7542371ed6d85c2c15050fc95f10ea99e0c428c400ee93e3b7a887e94'
    cookie = {'session': sessionid}
    response = requests.get("https://adventofcode.com/2024/day/1/input", cookies=cookie)
    return response.text.strip().split("\n")

def calculate_diff(list1, list2):
    sorted_list1 = sorted(map(int, list1))
    sorted_list2 = sorted(map(int, list2))
    return [abs(a - b) for a, b in zip(sorted_list1, sorted_list2)]

def calculate_total_distance(distance_list):
    return sum(distance_list)

def test_functions():
    testlist1 = [3, 4, 2, 1, 3, 3]
    testlist2 = [4, 3, 5, 3, 9, 3]
    test_input = [f"{a} {b}" for a, b in zip(testlist1, testlist2)]
    test_result = [2, 1, 0, 1, 2, 5]
    assert calculate_diff(testlist1, testlist2) == test_result
    assert simiulary_score(test_input) == 31 

def part1(inputlist):
    list1 = [int(line.split()[0]) for line in inputlist]
    list2 = [int(line.split()[1]) for line in inputlist]
    distance_list = calculate_diff(list1, list2)
    print(calculate_total_distance(distance_list))

def simiulary_score(inputlist):
    list1 = [int(line.split()[0]) for line in inputlist]
    list2 = [int(line.split()[1]) for line in inputlist]
    score = 0
    for number in list1:
        list2count = list2.count(number)
        adding_score = number * list2count
        score += adding_score
    return score

def part2(inputlist):
    print(simiulary_score(inputlist))

if __name__ == "__main__":
    inputlist = grab_input()
    test_functions()
    part1(inputlist)
    part2(inputlist)
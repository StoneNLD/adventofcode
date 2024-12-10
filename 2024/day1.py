#!/usr/bin/python3

import requests

def grab_input():
    sessionid = input("sessionid from cookie: ")
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
    test_result = [2, 1, 0, 1, 2, 5]
    assert calculate_diff(testlist1, testlist2) == test_result
    assert simiulary_score(inputlist) == 31 

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
    pass

if __name__ == "__main__":
    test_functions()
    inputlist = grab_input()
    part1(inputlist)
    simiulary_score(inputlist)
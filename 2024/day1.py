#!/usr/bin/python3

import requests

def grab_input():
    sessionid = input("sessionid from cookie: ")
    cookie = {'session': sessionid}
    puzzle_input = requests.get("https://adventofcode.com/2024/day/1/input", cookies=cookie)
    inputlist = puzzle_input.text.split("\n")[:-1]
    return inputlist

testlist1 = [3, 4, 2, 1, 3, 3]
testlist2 = [4, 3, 5, 3, 9, 3]
test_result = [2, 1, 0, 1, 2, 5]

def calculate_diff(inputlist1, inputlist2):
    inputlist1.sort()
    inputlist2.sort()
    distance_list = []
    for number in range(len(inputlist1)):
        diff = abs(inputlist1[number] - inputlist2[number])
        distance_list.append(diff)
    return distance_list

def calculate_total_distance(distance_list):
    total_distance = 0
    for distance in distance_list:
        total_distance += distance
    return total_distance

def test_function(testlist1, testlist2, test_result):
    assert calculate_diff(testlist1, testlist2) == test_result

if __name__ == "__main__":
    test_function(testlist1, testlist2, test_result)
    inputlist = grab_input()
    list1 = []
    for x in inputlist:
        line = x.split()
        list1.append(int(line[0]))
    list2 = []
    for x in inputlist:
        line = x.split()
        list2.append(int(line[1]))
    distance_list = calculate_diff(list1, list2)
    print(calculate_total_distance(distance_list))


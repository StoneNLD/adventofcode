#!/usr/bin/python3

import requests

def grab_input():
    sessionid = input("sessionid from cookie: ")
    cookie = {'session': sessionid}
    response = requests.get("https://adventofcode.com/2015/day/7/input", cookies=cookie)
    return response.text.strip().split("\n")

test_input_part1 = []
test_output = 4

test_input_part2 = []
test_output_part2 = 9


def test_function_part1():
    assert True == True

def test_function_part2():
    assert True == True

def part1():
    pass

def part2():
    pass

if __name__ == "__main__":
    inputlist = grab_input()
    test_function_part1()
    test_function_part2()
    part1(inputlist)
    part2(inputlist)
#!/usr/bin/python3

import requests

def grab_input():
    sessionid = input("sessionid from cookie: ")
    cookie = {'session': sessionid}
    response = requests.get("https://adventofcode.com/2015/day/7/input", cookies=cookie)
    return response.text.strip().split("\n")

circuit = [
    "123 -> x",
    "456 -> y",
    "x AND y -> d",
    "x OR y -> e",
    "x LSHIFT 2 -> f",
    "y RSHIFT 2 -> g",
    "NOT x -> h",
    "NOT y -> i"
]

signals = {
    "d": 72,
    "e": 507,
    "f": 492,
    "g": 114,
    "h": 65412,
    "i": 65079,
    "x": 123,
    "y": 456
}

def find_signal(wire, inputlist):
    for line in inputlist:
        if wire == line.split(" -> ")[1]:
             find_signal(line.split(" -> ")[0], inputlist)
             return line
    
    return None
        

def test_function_part1():
    assert True == True

def test_function_part2():
    assert True == True

def part1():
    print(find_signal("a", inputlist))

def part2():
    pass

if __name__ == "__main__":
    inputlist = grab_input()
    # print(inputlist)
    # test_function_part1()
    # test_function_part2()
    part1()
    # part2(inputlist)
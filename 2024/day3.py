#!/usr/bin/python3

import requests
import re

def grab_input():
    sessionid = input("sessionid from cookie: ")
    cookie = {'session': sessionid}
    response = requests.get("https://adventofcode.com/2024/day/3/input", cookies=cookie)
    return response.text.strip().split("\n")

test_input_part1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
test_input_part2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
test_output_part1 = 161
test_output_part2 = 48

def add_mul(input):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, input)
    
    value = 0
    for match in matches:
        value += int(match[0]) * int(match[1])
    return value

def add_mul_do_dont(input):
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"
    
    mul_matches = re.finditer(mul_pattern, input)
    do_matches = re.finditer(do_pattern, input)
    dont_matches = re.finditer(dont_pattern, input)    
    
    instructions = []
    for match in mul_matches:
        instructions.append((match.start(), 'mul', match.groups()))
    for match in do_matches:
        instructions.append((match.start(), 'do'))
    for match in dont_matches:
        instructions.append((match.start(), "dont"))
    
    instructions.sort()
    
    enabled = True
    value = 0
    for instruction in instructions:
        if instruction[1] == 'do':
            enabled = True
        elif instruction[1] == "dont":
            enabled = False
        elif instruction[1] == 'mul' and enabled:
            value += int(instruction[2][0]) * int(instruction[2][1])

    return value

def test_functions(test_input_part1, test_input_part2, test_output_part1, test_output_part2):
    assert add_mul(test_input_part1) == test_output_part1
    assert add_mul_do_dont(test_input_part2) == test_output_part2

def part1(inputlist):
    flattened_input = ''.join(inputlist)
    value = add_mul(flattened_input)
    print(value)
    
def part2(inputlist):
    flattened_input = ''.join(inputlist)
    value = add_mul_do_dont(flattened_input)
    print(value)

if __name__ == "__main__":
    inputlist = grab_input()
    # print(inputlist)
    test_functions(test_input_part1, test_input_part2, test_output_part1, test_output_part2)
    print(add_mul_do_dont(test_input_part2))
    part1(inputlist)
    part2(inputlist)
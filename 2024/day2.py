#!/usr/bin/python3

import requests

def grab_input():
    sessionid = input("sessionid from cookie: ")
    cookie = {'session': sessionid}
    response = requests.get("https://adventofcode.com/2024/day/2/input", cookies=cookie)
    return response.text.strip().split("\n")

test_input  = ['7 6 4 2 1', 
               '1 2 7 8 9',
               '9 7 6 2 1',
               '1 3 2 4 5',
               '8 6 4 4 1',
               '1 3 6 7 9']
test_result_part1 = 2
test_result_part2 = 4

def test_functions(test_input, test_result_part1, test_result_part2):
    assert count_safe_reports(test_input) == test_result_part1
    assert count_safe_reports_dampener(test_input) == test_result_part2

def count_safe_reports(test_input):
    safe_reports = 0
    for line in test_input:
        intarrayline = [int(x) for x in line.split()]
        if intarrayline == sorted(intarrayline) or intarrayline == sorted(intarrayline, reverse=True):
            if all(1 <= abs(intarrayline[i] - intarrayline[i + 1]) <= 3 for i in range(len(intarrayline) - 1)):
                safe_reports += 1
    # print(safe_reports)
    return safe_reports
        
def part1(inputlist):
    print(count_safe_reports(inputlist))

def count_safe_reports_dampener(test_input):
    def is_sorted_or_reverse_sorted(arr):
        ascending = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
        descending = all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
        return ascending or descending

    def is_safe(arr):
        return all(1 <= abs(arr[i] - arr[i + 1]) <= 3 for i in range(len(arr) - 1))

    safe_reports = 0
    for line in test_input:
        intarrayline = [int(x) for x in line.split()]
        if is_sorted_or_reverse_sorted(intarrayline) and is_safe(intarrayline):
            safe_reports += 1
        else:
            for i in range(len(intarrayline)):
                modified_line = intarrayline[:i] + intarrayline[i+1:]
                if is_sorted_or_reverse_sorted(modified_line) and is_safe(modified_line):
                    safe_reports += 1
                    break
    return safe_reports

def part2(inputlist):
    print(count_safe_reports_dampener(inputlist))

if __name__ == "__main__":
    inputlist = grab_input()
    # print(inputlist)
    test_functions(test_input, test_result_part1, test_result_part2)
    part1(inputlist)
    part2(inputlist)
#!/usr/bin/python3

import requests

def grab_input():
    sessionid = input("sessionid from cookie: ")
    cookie = {'session': sessionid}
    puzzle_input = requests.get("https://adventofcode.com/2022/day/6/input", cookies=cookie)
    inputlist = puzzle_input.text.split("\n")[:-1]
    return inputlist

def return_marker_postition(entry):
    for i in range(len(entry)-2):
        if entry[i:i+4].count(entry[i]) == 1:
            if entry[i+1:i+4].count(entry[i+1]) == 1:
                if entry[i+2:i+4].count(entry[i+2]) == 1:
                    return i+4

# This could obviously be smarter and better readable haha
def return_message_position(entry):       
    for i in range(len(entry)-2):
        if entry[i:i+14].count(entry[i]) == 1:
            if entry[i+1:i+14].count(entry[i+1]) == 1:
                if entry[i+2:i+14].count(entry[i+2]) == 1:
                    if entry[i+3:i+14].count(entry[i+3]) == 1:
                        if entry[i+4:i+14].count(entry[i+4]) == 1:
                            if entry[i+5:i+14].count(entry[i+5]) == 1:
                                if entry[i+6:i+14].count(entry[i+6]) == 1:
                                    if entry[i+7:i+14].count(entry[i+7]) == 1:
                                        if entry[i+8:i+14].count(entry[i+8]) == 1:
                                            if entry[i+9:i+14].count(entry[i+9]) == 1:
                                                if entry[i+10:i+14].count(entry[i+10]) == 1:
                                                    if entry[i+11:i+14].count(entry[i+11]) == 1:
                                                        if entry[i+12:i+14].count(entry[i+12]) == 1:
                                                            if entry[i+13:i+14].count(entry[i+13]) == 1:             
                                                                return i+14

# # should result to 5
# inputlist = "bvwbjplbgvbhsrlpgdmjqwftvncz"
# # should result to 11
# inputlist2 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
# # should return 10
# = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"

def test_function(testinput, result):
    assert return_marker_postition("".join(testinput)) == result 

def part1():
    print("Marker is placed at postition:", return_marker_postition("".join(inputlist)))

def part2():
    print("Message is placed at postition:", return_message_position("".join(inputlist)))

if __name__ == "__main__":
    inputlist = grab_input()
    test_function("bvwbjplbgvbhsrlpgdmjqwftvncz", 5)
    part1()
    part2()
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

def return_message_position(entry):       
    for i in range(len(entry)-2):
        if all(entry[i:i+14].count(char) == 1 for char in entry[i:i+14]):
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
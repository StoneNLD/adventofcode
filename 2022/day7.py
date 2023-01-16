#!/usr/bin/python3

import requests
import re
import itertools

def grab_input():
    sessionid = input("sessionid from cookie: ")
    cookie = {'session': sessionid}
    puzzle_input = requests.get("https://adventofcode.com/2022/day/7/input", cookies=cookie)
    inputlist = puzzle_input.text.split("\n")[:-1]
    return inputlist

inputlist = grab_input()
# inputlist = [
#     "$ cd /",
#     "$ ls",
#     "dir a",
#     "14848514 b.txt",
#     "8504156 c.dat",
#     "dir d",
#     "$ cd a",
#     "$ ls",
#     "dir e",
#     "29116 f",
#     "2557 g",
#     "62596 h.lst",
#     "$ cd e",
#     "$ ls",
#     "584 i",
#     "$ cd ..",
#     "$ cd ..",
#     "$ cd d",
#     "$ ls",
#     "4060174 j",
#     "8033020 d.log",
#     "5626152 d.ext",
#     "7214296 k",
#     ]

def get_file_system_directories(entry):
    cwd = ""
    directories = {"/home": 0}
    for line in entry:
        line = line.split()
        if line[0] == "$":
            if line[1] == "ls":
                pass
            else:
                if line[2] == "..":
                    # Find index of last occurrence of "/" and create new string until that index
                    cwd = cwd[:cwd.rindex("/")]
                elif line[2] == "/":
                    cwd = "/home"
                else:
                    cwd = cwd + "/" + line[2]
                    directories[cwd] = 0
        else:
            if line[0] != "dir":
                temp_path = cwd
                # Update all parent directories
                while temp_path != "":
                    directories[temp_path] += int(line[0])
                    temp_path = temp_path[:temp_path.rindex("/")]
    return directories

def part1():
    directories = get_file_system_directories(inputlist)
    sum_valid_directories = 0
    for _, directory in directories.items():
        if directory < 100000:
            sum_valid_directories += directory
    print("Total sum of valid dirs: " + str(sum_valid_directories))

def part2():
    directories = get_file_system_directories(inputlist)
    print(directories)
    required_free_space = directories["/home"] - (70000000 - 30000000) 
    smallest_deletable_directory = directories["/home"]
    for _, directory in directories.items():
        if required_free_space < directory < smallest_deletable_directory:
            smallest_deletable_directory = directory
    print("Smallest dir to delete " + str(smallest_deletable_directory))

if __name__ == "__main__":
    inputlist = grab_input()
    part1()
    part2()
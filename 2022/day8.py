#!/usr/bin/python3

import requests

def grab_input():
    sessionid = input("sessionid from cookie: ")
    cookie = {'session': sessionid}
    puzzle_input = requests.get("https://adventofcode.com/2022/day/8/input", cookies=cookie)
    inputlist = puzzle_input.text.split("\n")[:-1]
    return inputlist

# inputlist = grab_input()
#print(inputlist)

# inputlist = [
#     "30373",
#     "25512",
#     "65332",
#     "33549",
#     "35390"
# ]

def count_visible(inputlist):
    # exclude bordertrees
    visible_trees = len(inputlist)*2 + (len(inputlist[0])-2)*2  
    for row_index, row in enumerate(inputlist):
        # skip first and last
        if row_index == 0 or row_index == len(inputlist)-1:  
            continue
        for tree_index, tree_height in enumerate(row):
            # skip first and last
            if tree_index == 0 or tree_index == len(row)-1: 
                continue
            tree_height = int(tree_height)
            top_trees = [row[tree_index] for row in inputlist[:row_index]]
            bottom_trees = [row[tree_index] for row in inputlist[row_index+1:]]
            # check from al 4 sides and return True if visable
            visible_from_left = all(int(height) < tree_height for height in row[:tree_index])
            visible_from_right = all(int(height) < tree_height for height in row[tree_index+1:])        
            visible_from_top = all(int(height) < tree_height for height in top_trees)
            visible_from_bottom = all(int(height) < tree_height for height in bottom_trees)
            # add if at least visable from 1 side
            visible_trees += any([visible_from_left, visible_from_right, visible_from_top, visible_from_bottom])
    print("Visable Trees: " + str(visible_trees))

def part1():
    count_visible(inputlist)

def get_vision(tree_height, tree_list):
    vision = 0
    index = 0
    while index != len(tree_list):
        vision += 1
        if int(tree_list[index]) >= tree_height:  
            return vision
        index += 1
    return vision

def get_highest_score(inputlist):
    # Iterate over all the trees and check if the tree's combined visions is higher than the highest one until now
    highest_scenic_score = 0
    for row_index, row in enumerate(inputlist):
        if row_index == 0 or row_index == len(inputlist)-1:  # Skip first and last row
            continue
        for tree_index, tree_height in enumerate(row):
            if tree_index == 0 or tree_index == len(row)-1:  # Skip first and last column
                continue
            tree_height = int(tree_height)
            top_trees = [row[tree_index] for row in inputlist[:row_index]]
            bottom_trees = [row[tree_index] for row in inputlist[row_index+1:]]
            # get score from all sides
            left_vision = get_vision(tree_height, row[:tree_index:][::-1])
            right_vision = get_vision(tree_height, row[tree_index+1:])    
            top_vision = get_vision(tree_height, top_trees[::-1])          
            bottom_vision = get_vision(tree_height, bottom_trees)
            vision_score = left_vision * right_vision * top_vision * bottom_vision
            if vision_score > highest_scenic_score:
                highest_scenic_score = vision_score
    print("Highest scenic score: " + str(highest_scenic_score))

def part2():
   get_highest_score(inputlist)

if __name__ == "__main__":
    inputlist = grab_input()
    part1()
    part2()
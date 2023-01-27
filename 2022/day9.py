#!/usr/bin/python3

import requests

def grab_input():
    sessionid = input("sessionid from cookie: ")
    cookie = {'session': sessionid}
    puzzle_input = requests.get("https://adventofcode.com/2022/day/9/input", cookies=cookie)
    inputlist = puzzle_input.text.split("\n")[:-1]
    return inputlist

inputlist = grab_input()
print(inputlist)

def move_head_straight(part, direction):
    if direction == "R":
        part[0] += 1
    elif direction == "L":
        part[0] -= 1
    elif direction == "U":
        part[1] += 1
    elif direction == "D":
        part[1] -= 1


def move_tail_diagonally(head, tail):
    if head[0] > tail[0]:
        tail[0] += 1
    else:
        tail[0] -= 1
    if head[1] > tail[1]:
        tail[1] += 1
    else:
        tail[1] -= 1


def move_tail_straight(head, tail):
    if head[0] == tail[0]:
        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
    elif head[1] == tail[1]:
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1


def is_head_touching(head, tail):
    row_dist_from_head = abs(head[0] - tail[0])
    column_dist_from_head = abs(head[1] - tail[1])
    return max(row_dist_from_head, column_dist_from_head) <= 1


def fill_visited_pos(should, tail, dictionary):
    if should:
        dictionary.setdefault(tail[0], set()).add(tail[1])

def get_tail_visited_pos(rope, moves):
    tail_visited_pos = {0: {0}}
    for move in moves:
        move_direction, move_num = move.split()
        head = rope[0]
        for _ in range(int(move_num)):
            move_head_straight(head, move_direction)
            for knot_idx in range(len(rope)-1):
                temp_head, tail = rope[knot_idx], rope[knot_idx+1]
                if not is_head_touching(temp_head, tail):
                    is_last_tail = knot_idx+2 == len(rope)
                    if not (temp_head[0] == tail[0] or temp_head[1] == tail[1]):
                        move_tail_diagonally(temp_head, tail)
                        fill_visited_pos(is_last_tail, tail, tail_visited_pos)
                    while not is_head_touching(temp_head, tail):
                        move_tail_straight(temp_head, tail)
                        fill_visited_pos(is_last_tail, tail, tail_visited_pos)
                else:
                    break
    return tail_visited_pos

def part1(inputlist):
    rope = [[0, 0] for _ in range(2)]
    tail_visited_pos = get_tail_visited_pos(rope, inputlist)
    visited_pos_num = 0
    for row in tail_visited_pos.values():
        visited_pos_num += len(set(row))
    print("Part1 result: " + str(visited_pos_num))

def part2(inputlist):
    rope = [[0, 0] for _ in range(10)]
    tail_visited_pos = get_tail_visited_pos(rope, inputlist)
    visited_pos_num = 0
    for row in tail_visited_pos.values():
        visited_pos_num += len(row)
    print("Part2 result: " + str(visited_pos_num))

if __name__ == "__main__":
    inputlist = grab_input()
    part1(inputlist)
    part2(inputlist)


#!/usr/bin/python3

import requests

def grab_input():
    sessionid = input("sessionid from cookie: ")
    cookie = {'session': sessionid}
    response = requests.get("https://adventofcode.com/2024/day/4/input", cookies=cookie)
    return response.text.strip().split("\n")

test_input = [ "..X...",
               ".SAMX.",
               ".A..A.",
               "XMAS.S",
               ".X...."
              ]

test_output = 4

test_input_part2 = [
    ".M.S......",
    "..A..MSMS.",
    ".M.S.MAA..",
    "..A.ASMSM.",
    ".M.S.M....",
    "..........",
    "S.S.S.S.S.",
    ".A.A.A.A..",
    "M.M.M.M.M.",
    ".........."
]

test_output_part2 = 9

pattern = [
    "M.S",
    ".A.",
    "M.S"
]

def count_word_in_grid(grid, word):
    def search_from_position(x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != word[i]:
                return False
        return True

    directions = [
        (1, 0),  # horizontaal naar rechts
        (-1, 0),  # horizontaal naar links
        (0, 1),  # verticaal naar beneden
        (0, -1),  # verticaal naar boven
        (1, 1),  # diagonaal naar rechtsonder
        (-1, -1),  # diagonaal naar linksboven
        (1, -1),  # diagonaal naar linksonder
        (-1, 1)  # diagonaal naar rechtsboven
    ]

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if search_from_position(x, y, dx, dy):
                    count += 1

    return count

def count_xmas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for r in range(1, rows - 1):  # Skip borders
        for c in range(1, cols - 1):  # Skip borders
            if grid[r][c] == 'A':  # Center must be 'A'
                try:
                    # M . S
                    # . A .
                    # M . S
                    if (grid[r - 1][c - 1] == 'M' and # Top-left
                        grid[r + 1][c + 1] == 'S' and # Bottom-right
                        grid[r + 1][c - 1] == 'M' and # Bottom-left
                        grid[r - 1][c + 1] == 'S'): # Top-right
                        print(f"found pattern 1 at ({r}, {c})")
                        count += 1
                    # S . M
                    # . A .
                    # S . M
                    if (grid[r - 1][c - 1] == 'S' and # Top-left
                        grid[r + 1][c + 1] == 'M' and # Bottom-right
                        grid[r + 1][c - 1] == 'S' and # Bottom-left
                        grid[r - 1][c + 1] == 'M'): # Top-right
                        print(f"found pattern 2 at ({r}, {c})")
                        count += 1
                    # M . M
                    # . A .
                    # S . S
                    if (grid[r - 1][c - 1] == 'M' and # Top-left
                        grid[r + 1][c + 1] == 'S' and # Bottom-right
                        grid[r + 1][c - 1] == 'S' and # Bottom-left
                        grid[r - 1][c + 1] == 'M'): # Top-right
                        print(f"found pattern 3 at ({r}, {c})")
                        count += 1
                    # S . S
                    # . A .
                    # M . M
                    if (grid[r - 1][c - 1] == 'S' and # Top-left
                        grid[r + 1][c + 1] == 'M' and # Bottom-right
                        grid[r + 1][c - 1] == 'M' and # Bottom-left
                        grid[r - 1][c + 1] == 'S'): # Top-right
                        print(f"found pattern 4 at ({r}, {c})")
                        count += 1
                except IndexError:
                    # Ignore out-of-bounds checks
                    continue

    return count

def test_functions(test_input, test_output):
    assert count_word_in_grid(test_input, "XMAS") == test_output

def test_function_part2(test_input_part2, test_output_part2):
    assert count_xmas_patterns(test_input_part2) == test_output_part2

def part1(inputlist):
    print(count_word_in_grid(inputlist, "XMAS"))

def part2(inputlist):
    print(count_xmas_patterns(inputlist))
    

if __name__ == "__main__":
    inputlist = grab_input()
    # print(count_word_in_grid(test_input, "XMAS"))
    test_functions(test_input, test_output)
    test_function_part2(test_input_part2, test_output_part2)
    part1(inputlist)
    part2(inputlist)
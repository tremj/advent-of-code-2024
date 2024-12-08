from collections import deque
from time import sleep

def part1():
    with open("input.txt") as file:
        lines = file.read().splitlines()

    dirs = [
        (0, 1),   # right
        (1, 0),   # down
        (0, -1),  # left
        (-1, 0)   # up
    ]

    # find guard start point
    i, j = 0, 0
    row = len(lines)
    col = len(lines[0])
    for i in range(row):
        did_break = False
        for j in range(col):
            if not (lines[i][j] in {'.', '#'}):
                did_break = True
                break
        if did_break:
            break

    direction = 0

    match lines[i][j]:
        case '>':
            direction = 0
        case 'v':
            direction = 1
        case '<':
            direction = 2
        case '^':
            direction = 3

    unique = 0

    lines = [list(line) for line in lines]

    while True:
        next_i, next_j = i + dirs[direction][0], j + dirs[direction][1]
        if not (0 <= next_i < row) or not (0 <= next_j < col):
            lines[i][j] = 'X'
            unique += 1
            break
        elif lines[next_i][next_j] == '#':
            direction = (direction + 1) % 4

        if lines[i][j] != 'X':
            lines[i][j] = 'X'
            unique += 1
        i, j = i + dirs[direction][0], j + dirs[direction][1]
    return unique

def get_next_block(blocks, direction, row, col):
    if direction == 0: # up
        i = blocks[2][0] - 1
        j = blocks[0][1] - 1
        # print(i, j)
        if 0 <= i < row and 0 <= j < col:
            return (i, j)
    elif direction == 1: # left
        i = blocks[0][0] - 1
        j = blocks[2][1] + 1
        # print(i, j)
        if 0 <= i < row and 0 <= j < col:
            return (i, j)
    elif direction == 2: # down
        i = blocks[2][0] + 1
        j = blocks[0][1] + 1
        # print(i, j)
        if 0 <= i < row and 0 <= j < col:
            return (i, j)
    elif direction == 3: # right
        i = blocks[0][0] + 1
        j = blocks[2][1] - 1
        # print(i, j)
        if 0 <= i < row and 0 <= j < col:
            return (i, j)
    return (-1, -1)


def part2():
    with open("input.txt") as file:
        lines = file.read().splitlines()

    dirs = [
        (-1, 0),  # up
        (0, 1),   # right
        (1, 0),   # down
        (0, -1),  # left
    ]

    # find guard start point
    i, j = 0, 0
    row = len(lines)
    col = len(lines[0])
    for i in range(row):
        did_break = False
        for j in range(col):
            if not (lines[i][j] in {'.', '#'}):
                did_break = True
                break
        if did_break:
            break

    direction = 0

    match lines[i][j]:
        case '^':
            direction = 0
        case '>':
            direction = 1
        case 'v':
            direction = 2
        case '<':
            direction = 3

    blocks = 0

    lines = [list(line) for line in lines]

    last_3_blocks = deque()

    possible_obstacle = None
    while True:
        next_i, next_j = i + dirs[direction][0], j + dirs[direction][1]
        if not (0 <= next_i < row) or not (0 <= next_j < col):
            break

        # print(possible_obstacle)
        # print((next_i, next_j))
        if possible_obstacle == (next_i, next_j):
            # print("TARGET HIT")
            blocks += 1

        if lines[next_i][next_j] == '#':
            last_3_blocks.append((next_i, next_j))
            direction = (direction + 1) % 4
            if len(last_3_blocks) == 3:
                possible_obstacle = get_next_block(list(last_3_blocks), (direction + 1) % 4, row, col)
                last_3_blocks.popleft()

        lines[i][j] = 'X'

        # for line in lines:
        #     print(line)
        # # print("\n\n\n")
        # sleep(0.7)
        i, j = i + dirs[direction][0], j + dirs[direction][1]

    return blocks

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

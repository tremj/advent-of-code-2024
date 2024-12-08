# from time import sleep

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
        # for line in lines:
        #     print(line)
        # print("\n\n\n")
        # sleep(0.1)


    return unique

def part2():
    with open("test.txt") as file:
        lines = file.read().splitlines()



    return 0

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

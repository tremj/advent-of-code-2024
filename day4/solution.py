def dirs(i, j, lines):
    match = "XMAS"
    score = 0
    directions = [
        [[1, 0], [2, 0], [3, 0]], # south
        [[-1, 0], [-2, 0], [-3, 0]], # north
        [[0, 1], [0, 2], [0, 3]], # east
        [[0, -1], [0, -2], [0, -3]], # west
        [[1, 1], [2, 2], [3, 3]], # south-east
        [[1, -1], [2, -2], [3, -3]], # south-west
        [[-1, 1], [-2, 2], [-3, 3]], # north-east
        [[-1, -1], [-2, -2], [-3, -3]] # north-west
    ]
    for dir in directions:
        if 0 <= i + dir[2][0] < len(lines) and 0 <= j + dir[2][1] < len(lines[0]):
            possible_match = lines[i][j]
            for jump in dir:
                possible_match += lines[i+jump[0]][j+jump[1]]
            if possible_match == match:
                score += 1
    return score

def part1():
    with open("input.txt") as file:
        lines = file.read().splitlines()
    sum = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == 'X':
                sum += dirs(i, j, lines)
    return sum

def cross(i, j, lines):
    # M
    #  A
    #   S
    if lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S':
        # M S
        #  A
        # M S
        if lines[i+1][j-1] == 'M' and lines[i-1][j+1] == 'S':
            return 1
        # M M
        #  A
        # S S
        elif lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S':
            return 1
    # S
    #  A
    #   M
    elif lines[i+1][j+1] == 'M' and lines[i-1][j-1] == 'S':
        # S S
        #  A
        # M M
        if lines[i+1][j-1] == 'M' and lines[i-1][j+1] == 'S':
            return 1
        # S M
        #  A
        # S M
        elif lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S':
            return 1
    return 0

def part2():
    with open("input.txt") as file:
        lines = file.read().splitlines()
    sum = 0
    # don't worry about about array bounds now
    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[0])-1):
            if lines[i][j] == 'A':
                sum += cross(i, j, lines)
    return sum

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

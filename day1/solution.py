def part1():
    file = open("input.txt")
    left = list()
    right = list()
    for line in file.readlines():
        left.append(int(line[0:5]))
        right.append(int(line[-6:-1]))
    file.close()
    left.sort()
    right.sort()
    sum = 0
    for i in range(len(left)):
        sum += abs(left[i] - right[i])

    return sum

def part2():
    file = open("input.txt")
    left = list()
    right = dict()
    for line in file.readlines():
        left.append(int(line[0:5]))
        right[int(line[-6:-1])] = 1 + right.get(int(line[-6:-1]), 0)
    file.close()
    sum = 0
    for num in left:
        sum += num * right.get(num, 0)

    return sum

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

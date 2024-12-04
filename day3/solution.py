import re

def part1():
    with open("input.txt") as file:
        lines = file.read().splitlines()

    sum = 0
    pattern = r"mul\((\d+),(\d+)\)"
    for line in lines:
        matches = re.findall(pattern, line)
        for x, y in matches:
            sum += int(x) * int(y)
    return sum

def part2():
    with open("input.txt") as file:
        text = file.read().replace('\n', '')
    sum = 0
    mul_pattern = r"mul\((\d+),(\d+)\)"
    start_pattern = r"^(.*?)don\'t\(\)"
    enable_pattern = r"do\(\)(.*?)don\'t\(\)"
    end_pattern = r"do\(\)(?!.*do\(\))(.*)"
    instructions = ""
    instructions += re.search(start_pattern, text).group(0)
    instructions += re.search(end_pattern, text).group(0)

    enabled_matches = re.findall(enable_pattern, text)
    for match in enabled_matches:
        instructions += match

    matches = re.findall(mul_pattern, instructions)
    for x, y in matches:
        sum += int(x) * int(y)
    return sum

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

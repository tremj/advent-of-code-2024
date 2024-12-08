from functools import cmp_to_key

def make_line_valid(line, rules):
    def my_comparator(item1, item2):
        if item2 in rules.get(item1, set()):
            return -1
        if item1 in rules.get(item2, set()):
            return 1
        return 0

    return sorted(line, key=cmp_to_key(my_comparator))

def sol():
    with open("input.txt") as file:
        lines = file.read().splitlines()

    rules = dict()
    i = 0
    while len(lines[i]) >= 2:
        rule = lines[i].strip().split('|')
        if rules.get(int(rule[0]), {}) == {}:
            rules[int(rule[0])] = set()
            rules[int(rule[0])].add(int(rule[1]))
        else:
            rules[int(rule[0])].add(int(rule[1]))
        i += 1

    # PART 1
    sum_1 = 0
    invalid_lines = []
    for j in range(i+1, len(lines)):
        elements = [int(x) for x in lines[j].strip().split(',')]
        valid = True
        seen = set()
        for num in elements:
            if any(required in seen for required in rules.get(num, set())):
                valid = False
                invalid_lines.append(elements)
                break
            seen.add(num)
        sum_1 += valid * elements[int(len(elements) / 2)]

    # Part 2
    sum_2 = 0
    for line in invalid_lines:
        validated_line = make_line_valid(line, rules)
        sum_2 += validated_line[len(line)//2]
    return sum_1, sum_2

if __name__ == "__main__":
    part1, part2 = sol()
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")

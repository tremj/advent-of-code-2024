def part1():
    file = open("/Users/trem/Desktop/AdventOfCode/2024/AdventOfCodeJT-2024/day2/input.txt")
    safe = 0
    for line in file.readlines():
        nums = [int(x) for x in line.strip().split(' ')]
        unsafe = False
        increasing = False
        if (nums[0] < nums[1]):
            increasing = True
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff < 0 and increasing:
                unsafe = True
                break
            elif diff > 0 and not increasing:
                unsafe = True
                break
            diff = abs(diff)
            if not (1 <= diff and diff <= 3):
                unsafe = True
                break
        if not unsafe:
            safe += 1
    return safe

def is_safe(nums, can_skip):
    if len(nums) < 2:
        return True
    if nums[0] == nums[1]:
        return can_skip and (is_safe(nums[1:], False) or is_safe([nums[0]] + nums[2:], False))
    increasing = nums[0] < nums[1]
    for i in range(1, len(nums)):
        if not (1 <= abs(nums[i] - nums[i-1]) <= 3):
            return can_skip and (is_safe(nums[:i] + nums[i+1:], False) or is_safe(nums[:i-1] + nums[i:], False))
        else:
            if increasing and nums[i-1] < nums[i]:
                continue
            elif not increasing and nums[i-1] > nums[i]:
                continue
            return can_skip and (is_safe(nums[:i] + nums[i+1:], False) or is_safe(nums[:i-1] + nums[i:], False))
    return True

def part2():
    file = open("input.txt")
    safe = 0
    for line in file.readlines():
        nums = [int(x) for x in line.strip().split(' ')]
        if is_safe(nums, True) or is_safe(nums[1:], False):
            safe += 1
    return safe


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

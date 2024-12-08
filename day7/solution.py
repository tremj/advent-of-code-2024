from time import time

def part1():
    with open("input.txt") as file:
        lines = file.read().splitlines()

    sum = 0

    for line in lines:
        target, nums = line.split(': ')
        target = int(target)
        nums = [int(x) for x in nums.split(' ')]
        n = len(nums)
        possibilities = 2 ** (n-1)
        for b in range(possibilities):
            res = nums[0]
            for i in range(1, n):
                if b & (1 << (i-1)):
                    res *= nums[i]
                else:
                    res += nums[i]
            if res == target:
                sum += target
                break
    return sum

def part2():
    with open("input.txt") as file:
        lines = file.read().splitlines()

    sum = 0
    for line in lines:
        target, nums = line.split(': ')
        target = int(target)
        nums = [int(x) for x in nums.split(' ')]
        n = len(nums)
        possibilities = 3 ** (n-1)
        for t in range(possibilities):
            res = nums[0]
            for i in range(1, n):
                op = t % 3
                if op == 0:
                    res += nums[i]
                elif op == 1:
                    res *= nums[i]
                elif op == 2:
                    res = int(str(res) + str(nums[i]))
                t //= 3
            if res == target:
                sum += target
                break
    return sum

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")

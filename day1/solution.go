package day1

import (
	"bufio"
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func abs(x int) int {
	if x < 0 {
		return x * -1
	}
	return x
}

func Part1() int {
	file, err := os.Open("day1/input.txt")
	if err != nil {
		fmt.Println("Error: ", err)
		return -1
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var left, right []int

	for scanner.Scan() {
		line := strings.Split(scanner.Text(), "   ")
		leftNum, _ := strconv.Atoi(line[0])
		rightNum, _ := strconv.Atoi(strings.TrimSpace(line[1]))
		left = append(left, leftNum)
		right = append(right, rightNum)
	}

	slices.Sort(left)
	slices.Sort(right)
	sum := 0

	for i := 0; i < len(left); i++ {
		sum += abs(left[i] - right[i])
	}
	return sum
}

type IntMap map[int]int

func (m IntMap) addHelper(num int) {
	_, exists := m[num]
	if !exists {
		m[num] = 1
	} else {
		m[num] += 1
	}
}

func (m IntMap) getHelper(num int) int {
	value, exists := m[num]
	if !exists {
		return 0
	}
	return value
}

func Part2() int {
	file, err := os.Open("day1/input.txt")
	if err != nil {
		fmt.Println("Error: ", err)
		return -1
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var left []int
	right := make(IntMap)

	for scanner.Scan() {
		line := strings.Split(scanner.Text(), "   ")
		leftNum, _ := strconv.Atoi(line[0])
		rightNum, _ := strconv.Atoi(strings.TrimSpace(line[1]))
		left = append(left, leftNum)
		right.addHelper(rightNum)
	}

	sum := 0

	for i := 0; i < len(left); i++ {
		sum += left[i] * right.getHelper(left[i])
	}

	return sum
}

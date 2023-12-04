import os
import cProfile
import pstats
import re
from collections import defaultdict

from adventofcode.solutions.y2023.d03.part1 import parse, find_adjacent_index


def solve(data, size):
    solution = 0

    gears = defaultdict(set)

    for found_number in re.finditer(r"\d+", data):
        number = int(found_number.group())
        position = found_number.start(), found_number.end()

        for i in range(position[0], position[-1]):
            new_adjacent = find_adjacent_index(i, size)
            for index in new_adjacent:
                if data[index] == "*":
                    gears[index].add(number)

    solution = 0
    for numbers in gears.values():
        numbers = list(numbers)
        if len(numbers) > 1:
            solution += numbers[0] * numbers[1]

    return solution


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data, size = parse(file)

    return solve(data, size)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

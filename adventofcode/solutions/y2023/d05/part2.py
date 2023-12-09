import os
import cProfile
import pstats
import re

from adventofcode.solutions.y2023.d05.part1 import parse, parse_map, solve


def parse_seed(line):
    line = line.strip("\n")
    m = re.findall(r"\d+\s+\d+", line)
    ranges = []
    for index, couple in enumerate(m):
        from_value, offset = couple.split(" ")
        from_value = int(from_value)
        to_value = from_value + int(offset)
        ranges.append(range(from_value, to_value))

    return ranges


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file, parse_seed_func=parse_seed)

    return solve(*data) - 1


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

import os
import cProfile
import pstats

from adventofcode.solutions.y2022.d01.part1 import parse


def solve(elfs):
    max_values = [-1] * 3

    for e in elfs:
        value = sum(e)

        max_values.append(value)

        min_value = min(max_values)
        min_index = max_values.index(min_value)

        max_values.pop(min_index)

    return sum(max_values)


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        elfs = parse(file)

    return solve(elfs)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

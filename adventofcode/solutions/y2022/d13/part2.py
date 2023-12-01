import os
import cProfile
import pstats
import functools

from adventofcode.solutions.y2022.d13.part1 import compare


def parse(file):
    signals = []
    for line in file:
        line = line.strip("\n")

        if len(line) == 0:
            continue

        signals.append(eval(line))

    return signals


def solve(data, dividers):
    data += dividers

    res = sorted(data, key=functools.cmp_to_key(compare))

    divider_indexes = []
    for divider in dividers:
        divider_indexes.append(res.index(divider) + 1)

    return divider_indexes[0] * divider_indexes[1]


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    dividers = [[[2]], [[6]]]

    return solve(data, dividers)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

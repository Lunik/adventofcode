import os
import cProfile
import pstats

from adventofcode.solutions.y2022.d05.part1 import parse


def solve(matrix, instructions):
    for count, from_tower, to_tower in instructions:
        buffer = matrix[from_tower - 1][-count:]
        matrix[from_tower - 1] = matrix[from_tower - 1][:-count]

        matrix[to_tower - 1] += buffer

    res = ""

    for column in matrix:
        res += column.pop()

    return res


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    return solve(*data)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

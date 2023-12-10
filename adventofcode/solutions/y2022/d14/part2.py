import os
import cProfile
import pstats
from copy import copy

from adventofcode.solutions.y2022.d14.part1 import parse


def check_move(sand, data, floor):
    possible = [
        (sand[0], sand[1] + 1),
        (sand[0] - 1, sand[1] + 1),
        (sand[0] + 1, sand[1] + 1),
    ]

    for p in possible:
        if p[1] < floor and (p not in data):
            return p

    return False


def move(sand, data, floor):
    new_sand = check_move(sand, data, floor)
    if not new_sand:
        return False

    while new_sand != sand:
        sand = new_sand
        new_sand = check_move(sand, data, floor)
        if not new_sand:
            return sand


def solve(data, start):
    floor = max([p[1] for p in data.keys()]) + 2

    sand_count = 0
    while True:
        sand = copy(start)
        new_sand = move(sand, data, floor)

        sand_count += 1

        if not new_sand:
            break

        data[new_sand] = "o"

    return sand_count


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    start = (500, 0)

    return solve(data, start)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

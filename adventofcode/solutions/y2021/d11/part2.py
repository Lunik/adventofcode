import os
import cProfile
import pstats

from adventofcode.solutions.y2021.d11.part1 import parse, resolve_loop


def resolve(grid):
    total_flash = 0

    count_octopus = len(grid) * len(grid[0])

    step = 0
    while True:
        step += 1

        res = resolve_loop(grid)
        if res == count_octopus:
            return step

        total_flash += res


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        grid = parse(file)

    return resolve(grid)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

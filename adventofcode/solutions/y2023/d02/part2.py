import os
import cProfile
import pstats
from functools import reduce
import operator

from adventofcode.solutions.y2023.d02.part1 import (
    parse,
    construct_viewed,
    available_colors,
)


def solve(games, available_colors):
    solution = 0

    for game in games:
        construct_viewed(game)
        values = [game["viewed"][color_name] for color_name in available_colors]
        solution += reduce(operator.mul, values, 1)

    return solution


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    return solve(data, available_colors)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

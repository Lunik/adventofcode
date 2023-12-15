import os
import cProfile
import pstats

from adventofcode.solutions.y2023.d09.part1 import parse, solve


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    new_data = [list(reversed(sequence)) for sequence in data]

    return solve(new_data)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

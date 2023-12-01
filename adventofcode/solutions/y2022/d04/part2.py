import os
import cProfile
import pstats

from adventofcode.solutions.y2022.d04.part1 import parse


def solve(pairs):
    score = 0

    for pair_1, pair_2 in pairs:
        set_1 = set(range(pair_1[0], pair_1[1] + 1))
        set_2 = set(range(pair_2[0], pair_2[1] + 1))

        intersection = set_1.intersection(set_2)

        if len(intersection):
            score += 1

    return score


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    return solve(data)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

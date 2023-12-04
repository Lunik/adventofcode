import os
import cProfile
import pstats

from adventofcode.solutions.y2023.d04.part1 import parse


def solve(cards):
    multipliers = [1] * len(cards)

    for index, card in enumerate(cards):
        intersection = card[0].intersection(card[1])

        count = len(intersection)
        if count > 0:
            for i in range(index, index + count):
                multipliers[i + 1] += 1 * multipliers[index]

    return sum(multipliers)


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

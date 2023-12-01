import os
import cProfile
import pstats

from adventofcode.solutions.y2022.d02.part1 import parse, RULE


def solve(cheatsheet):
    score = 0

    for elf, todo in cheatsheet:
        score += 3 * todo

        if todo == 1:  # draw
            score += elf + 1
        elif todo == 0:  # lose
            score += RULE[elf] + 1
        else:  # win
            score += RULE.index(elf) + 1

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

import os
import cProfile
import pstats

from adventofcode.solutions.y2022.d10.part1 import parse, OP_CYCLES


def solve(instructions):
    X = 1
    cycle = 0
    signal_strength = None

    result = []

    for op, arg in instructions:
        for i in range(OP_CYCLES[op]):
            row = cycle // 40
            column = cycle % 40
            cycle += 1
            if len(result) <= row:
                result.append([])

            result[row].append("#" if column in [X - 1, X, X + 1] else ".")

        if op == "addx":
            X += arg

    return result


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    result = solve(data)

    return result


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

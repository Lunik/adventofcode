import os
import cProfile
import pstats
import re

from adventofcode.solutions.y2022.d15.part1 import parse, dist


def solve(data):
    possible = set()

    for sensor, beacon in data.items():
        for x in range(
            max(0, sensor[0] - beacon[1] - 1), min(4000000 + 1, sensor[0] + 1)
        ):
            y_1 = sensor[1] + (sensor[0] - beacon[1] - 1 - x)
            y_2 = sensor[1] - (sensor[0] - beacon[1] - 1 - x)

            if y_1 > 0 and y_1 <= 4000000 + 1:
                possible.add((x, y_1))
            if y_2 > 0 and y_2 <= 4000000 + 1:
                possible.add((x, y_2))

        for x in range(
            max(0, sensor[0] + 1), min(4000000 + 1, sensor[0] + 1 + beacon[1] + 1)
        ):
            y_1 = sensor[1] - (sensor[0] + 1 + beacon[1] - x)
            y_2 = sensor[1] + (sensor[0] + 1 + beacon[1] - x)

            if y_1 > 0 and y_1 <= 4000000 + 1:
                possible.add((x, y_1))
            if y_2 > 0 and y_2 <= 4000000 + 1:
                possible.add((x, y_2))

        total = len(possible)

    solution = None

    for index, pos in enumerate(possible):
        is_valid = True
        for sensor, beacon in data.items():
            distance = dist(pos, sensor)

            if distance <= beacon[1] or pos == beacon[0]:
                is_valid = False
                break

        if is_valid:
            solution = pos
            break

    return (solution[0] * 4000000) + solution[1]


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

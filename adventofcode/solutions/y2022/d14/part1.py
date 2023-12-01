import os
import cProfile
import pstats
import re
from copy import copy


def parse(file):
    data = dict()

    for line in file:
        line = line.strip("\n")
        res = re.findall(r"(\d+),(\d+)", line)

        for index in range(len(res) - 1):
            source = res[index]
            destination = res[index + 1]

            r1 = sorted([int(source[0]), int(destination[0])])
            r2 = sorted([int(source[1]), int(destination[1])])

            for i in range(r1[0], r1[1] + 1):
                for j in range(r2[0], r2[1] + 1):
                    data[(i, j)] = "#"

    return data


def check_move(sand, data):
    possible = [
        (sand[0], sand[1] + 1),
        (sand[0] - 1, sand[1] + 1),
        (sand[0] + 1, sand[1] + 1),
    ]

    for p in possible:
        if p not in data:
            return p

    return False


class Void(Exception):
    pass


def move(sand, data, deeper):
    new_sand = check_move(sand, data)
    while new_sand != sand:
        sand = new_sand
        new_sand = check_move(sand, data)
        if not new_sand:
            return sand

        if new_sand[1] > deeper:
            raise Void(f"Too deep {new_sand}")


def solve(data, start):
    deeper = max([p[1] for p in data.keys()])

    sand_count = 0
    while True:
        sand = copy(start)
        try:
            new_sand = move(sand, data, deeper)
        except Void as e:
            break

        data[new_sand] = "o"
        sand_count += 1

    return sand_count


def print_data(data):
    range_x = [p[0] for p in data.keys()]
    range_y = [p[1] for p in data.keys()]

    for y in range(min(range_y), max(range_y) + 1):
        line = []

        for x in range(min(range_x), max(range_x) + 1):
            if (x, y) in data:
                line.append(data[(x, y)])
            else:
                line.append(".")

        print("".join(line))


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

import os
import cProfile
import pstats
import re


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def parse(file):
    data = dict()

    for line in file:
        line = line.strip("\n")
        res = re.findall(r"x=(-?\d+), y=(-?\d+)", line)

        sensor = (int(res[0][0]), int(res[0][1]))
        beacon = (int(res[1][0]), int(res[1][1]))

        data[sensor] = (beacon, dist(sensor, beacon))

    return data


def solve(data, y):
    max_x = max(
        max([p[0] for p in data.keys()]),
        max([p[0][0] for p in data.values()]),
        max([s[0] + b[1] for s, b in data.items()]),
    )
    min_x = min(
        min([p[0] for p in data.keys()]),
        min([p[0][0] for p in data.values()]),
        min([s[0] - b[1] for s, b in data.items()]),
    )

    count = set()

    for x in range(min_x, max_x + 1):
        pos = (x, y)
        for sensor, beacon in data.items():
            distance = dist(pos, sensor)

            if distance <= beacon[1] and pos != beacon[0]:
                count.add(pos)
                break

    return len(count)


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    return solve(data, 2000000)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

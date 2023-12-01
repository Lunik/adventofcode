import os
import cProfile
import pstats
from adventofcode.solutions.y2022.d12.part1 import find_path


def locate(array, char):
    res = []

    for index, c in enumerate(array):
        if c == char:
            res.append(index)

    return res


def parse(file):
    matrix = []

    starts = []
    end = None

    for index, line in enumerate(file):
        line = list(line.strip("\n"))

        starts += list(map(lambda y: (index, y), locate(line, "a")))

        if "E" in line:
            y = line.index("E")
            line[y] = "z"
            end = (index, y)

        matrix.append(line)

    return matrix, starts, end


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        matrix, starts, end = parse(file)

    results = []
    for start in starts:
        res = find_path(matrix, start, end)
        if res:
            results.append(res[end])

    return min(results)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

import os
import cProfile
import pstats
import re


def parse(file):
    part = 0

    matrix = []
    instructions = []

    for line in file:
        line = line.strip("\n")

        if "1" in line and part == 0:
            part += 1
            continue

        if line == "":
            part += 1
            continue

        if part == 0:
            x = 1
            row = list(map(lambda x: x if x != " " else None, line[1::4]))
            matrix.append(row)

        if part == 2:
            res = re.match(r"move (\d+) from (\d+) to (\d+)", line)
            instructions.append(
                (int(res.group(1)), int(res.group(2)), int(res.group(3)))
            )

    new_matrix = []

    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])

        row.reverse()
        row = list(filter(lambda x: x, row))
        new_matrix.append(row)

    return new_matrix, instructions


def solve(matrix, instructions):
    for count, from_tower, to_tower in instructions:
        buffer = matrix[from_tower - 1][-count:]
        buffer.reverse()
        matrix[from_tower - 1] = matrix[from_tower - 1][:-count]

        matrix[to_tower - 1] += buffer

    res = ""

    for column in matrix:
        res += column.pop()

    return res


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    return solve(*data)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

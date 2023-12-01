import os
import cProfile
import pstats

from functools import reduce

import re


def parse_line(raw_line):
    regex = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")

    result = re.match(regex, raw_line)
    groups = result.groups()

    return ((int(groups[0]), int(groups[1])), (int(groups[2]), int(groups[3])))


def parse(raw_data):
    return [parse_line(raw_line) for raw_line in raw_data]


def compare(number_a, number_b):
    if number_a > number_b:
        result = -1
    elif number_b > number_a:
        result = 1
    else:
        result = 0

    return result


def vector_equal(vector_a, vector_b):
    return vector_a[0] == vector_b[0] and vector_a[1] == vector_b[1]


def calculate_line(vector, points):
    points.append(vector[0])
    step_x = compare(vector[0][0], vector[1][0])
    step_y = compare(vector[0][1], vector[1][1])

    last_point = vector[0]
    while not vector_equal(last_point, vector[1]):
        new_point = (last_point[0] + step_x, last_point[1] + step_y)
        points.append(new_point)
        last_point = new_point


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        vectors = parse(file.readlines())

    vectors = filter(lambda v: v[0][0] == v[1][0] or v[0][1] == v[1][1], vectors)

    lines = []
    for vector in vectors:
        calculate_line(vector, lines)

    counter = {}
    for point in lines:
        if str(point) not in counter:
            counter[str(point)] = 0
        counter[str(point)] += 1

    result = reduce(lambda a, b: a + b, map(lambda v: int(v >= 2), counter.values()))

    return result


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

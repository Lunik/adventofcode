import os

from functools import reduce


from adventofcode.solutions.y2020.d03.part1 import parse_line, verify


def main():
    the_map = []

    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        for line in file:
            the_map.append(parse_line(line))

    trees_count = []
    for move in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        trees_count.append(verify(the_map, move))

    return reduce(lambda a, b: a * b, trees_count)


if __name__ == "__main__":
    print(main())

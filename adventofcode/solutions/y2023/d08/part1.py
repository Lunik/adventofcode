import os
import cProfile
import pstats
import re

node_regex = re.compile(r"(?P<from>\w+) = \((?P<left>\w+), (?P<right>\w+)\)")


def parse_node(line):
    match = node_regex.match(line)
    groups = match.groupdict()
    return groups["from"], (groups["left"], groups["right"])


def parse(file):
    sequence = file.readline().strip("\n")
    _ = file.readline()

    data = {}

    for line in file:
        node_name, node_data = parse_node(line.strip("\n"))
        data[node_name] = node_data

    return sequence, data


def solve(sequence, data, source="AAA", destination="ZZZ"):
    steps = 0

    current = source
    while current != destination:
        step_orientation = sequence[steps % len(sequence)]
        if step_orientation == "L":
            current = data[current][0]
        elif step_orientation == "R":
            current = data[current][1]

        steps += 1

    return steps


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

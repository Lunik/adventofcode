import os
import cProfile
import pstats
import math

from adventofcode.solutions.y2023.d08.part1 import parse


def not_need_more_to_resolve(steps_to_end):
    for step in steps_to_end:
        if step == -1:
            return False

    return True


def solve(sequence, data):
    steps = 0

    currents = list(filter(lambda x: x[-1] == "A", data.keys()))
    steps_to_end = [-1] * len(currents)
    while not not_need_more_to_resolve(steps_to_end):
        step_orientation = sequence[steps % len(sequence)]
        for index, current in enumerate(currents):
            if steps_to_end[index] != -1:
                continue

            if step_orientation == "L":
                currents[index] = data[current][0]
            elif step_orientation == "R":
                currents[index] = data[current][1]

            if currents[index][-1] == "Z":
                steps_to_end[index] = steps + 1

        steps += 1

    lcm = steps_to_end[0]
    for n in steps_to_end[1:]:
        lcm = math.lcm(lcm, n)

    return lcm


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

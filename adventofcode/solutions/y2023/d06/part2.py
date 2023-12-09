import os
import cProfile
import pstats
import re

from adventofcode.solutions.y2023.d06.part1 import solve


def parse(file):
    races = []

    times = [file.readline().split(":")[1].replace(" ", "")]
    distance = [file.readline().split(":")[1].replace(" ", "")]

    for i in range(len(times)):
        races.append({"time": int(times[i]), "max_distance": int(distance[i])})

    return races


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

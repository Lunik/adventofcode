import os
import cProfile
import pstats


def parse(file):
    bags = []

    for line in file:
        line = line.strip("\n")

        bag = [line[: int(len(line) / 2)], line[int(len(line) / 2) :]]

        bags.append(bag)

    return bags


PRIORITIES = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def solve(bags):
    score = 0

    for bag in bags:
        part1 = set(bag[0])
        part2 = set(bag[1])

        intersection = list(part1.intersection(part2))
        score += PRIORITIES.index(intersection[0])

    return score


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

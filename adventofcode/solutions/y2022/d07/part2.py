import os
import cProfile
import pstats

from adventofcode.solutions.y2022.d07.part1 import parse, get_size


def solve(tree, needed_free_space):
    candidates = []

    if tree[0] == "f":
        return None

    if tree[0] == "d":
        if tree[2] > needed_free_space:
            candidates.append(tree[2])

        for child in tree[3]:
            res = solve(child, needed_free_space)
            if res:
                candidates.append(res)

    if len(candidates):
        return min(candidates)

    return None


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    get_size(data)

    total_size = 70000000
    free_space = total_size - data[2]
    required_free_space = 30000000

    return solve(data, required_free_space - free_space)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

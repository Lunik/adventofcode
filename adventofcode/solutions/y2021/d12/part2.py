import os
import cProfile
import pstats
import re
from copy import copy

from adventofcode.solutions.y2021.d12.part1 import parse, debug_cave


def find_path(cave, selected_small_cave, node="start", path=[]):
    p = copy(path)
    p.append(node)

    results = set()

    for neighbors in cave[node]:
        # Found the end, Stop and save the path
        if neighbors == "end":
            p2 = copy(p)
            p2.append(neighbors)
            results.add(";".join(p2))
            continue

        if neighbors in p:
            # Already walked cave
            if re.match(r"[A-Z]+", neighbors):
                # It's large cave, continue exploring
                results = results.union(
                    find_path(cave, selected_small_cave, neighbors, p)
                )
            elif neighbors == selected_small_cave:
                # It's the allowed small cave
                results = results.union(find_path(cave, None, neighbors, p))
            else:
                # It's a small cave
                # Dead end, Abort
                continue
        else:
            # New cave, continue exploring
            results = results.union(find_path(cave, selected_small_cave, neighbors, p))

    return results


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        cave = parse(file)

    full_res = set()

    for c in filter(
        lambda c: re.match(r"[a-z]+", c) and c not in ["start", "end"], cave
    ):
        full_res = full_res.union(find_path(cave, c))

    return len(full_res)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

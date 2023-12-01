import os
import cProfile
import pstats
import re


def parse(file):
    pairs = []

    for line in file:
        line = line.strip("\n")

        res = re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line)

        pairs.append(
            (
                (int(res.group(1)), int(res.group(2))),
                (int(res.group(3)), int(res.group(4))),
            )
        )

    return pairs


def solve(pairs):
    score = 0

    for pair_1, pair_2 in pairs:
        set_1 = set(range(pair_1[0], pair_1[1] + 1))
        set_2 = set(range(pair_2[0], pair_2[1] + 1))

        union = set_1.union(set_2)

        if union == set_1 or union == set_2:
            score += 1

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

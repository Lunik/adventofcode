import os
import cProfile
import pstats

from adventofcode.solutions.y2021.d06.part1 import (
    generate_pool,
    parse_data,
    run_loop,
    count_fish,
)


def main():
    pool = generate_pool()

    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        line = file.read()

    parse_data(line, pool)

    run_loop(256, pool)

    return count_fish(pool)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

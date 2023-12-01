import os
import cProfile
import pstats
import re

not_numbers = re.compile(r"[^\d]")


def main():
    solution = 0
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        for line in file:
            partial_solution = not_numbers.sub("", line)

            solution += int(partial_solution[0] + partial_solution[-1])

    return solution


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

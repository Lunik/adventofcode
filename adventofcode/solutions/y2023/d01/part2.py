import os
import cProfile
import pstats
import re

# '?=' allows to match overlapping patterns
number_re = re.compile(r"(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))")
traduction = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def main():
    solution = 0
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        for index, line in enumerate(file):
            potential_numbers = number_re.findall(line)

            solution += int(
                traduction[potential_numbers[0]] + traduction[potential_numbers[-1]]
            )

    return solution


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

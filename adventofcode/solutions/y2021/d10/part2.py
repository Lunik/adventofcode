import os
import cProfile
import pstats


from adventofcode.solutions.y2021.d10.part1 import PAIRING_CHAR, ExpectingChar


MISSING_CHAR_POINTS = {")": 1, "]": 2, "}": 3, ">": 4}


class MissingChars(Exception):
    def __init__(self, message, chars):
        super().__init__(message)

        self.chars = chars


def check_line(line):
    counter = []
    # print(f"\nline: {line}")
    for char in list(line):
        if char in "({[<":
            counter += char
        elif char in ")}]>" and counter[-1] == PAIRING_CHAR[char]:
            counter = counter[:-1]
        else:
            raise ExpectingChar(
                f"Expected {PAIRING_CHAR[counter[-1]]}, but found {char} instead.", char
            )

    missing_chars = ""
    while counter:
        char = counter.pop()
        missing_chars += PAIRING_CHAR[char]

    if len(missing_chars) > 0:
        raise MissingChars(f"Complete by adding {missing_chars}", missing_chars)

    return True


def solve(line):
    result = 0

    try:
        check_line(line)
    except ExpectingChar as _:
        # print(_)
        pass
    except MissingChars as _:
        # print(_)
        for char in _.chars:
            result = (result * 5) + MISSING_CHAR_POINTS[char]

    return result


def main():
    results = []
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        for line in file:
            result = solve(line.strip("\n"))
            if result > 0:
                results.append(result)

    results.sort()

    return results[round(len(results) / 2)]


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

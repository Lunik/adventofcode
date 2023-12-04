import os
import cProfile
import pstats
import re


def parse(file):
    data = file.read().splitlines()
    size = {"width": len(data[0]), "height": len(data)}  # width, height

    data = "".join(data)
    size["total"] = len(data)

    return data, size


def find_adjacent_index(index, size):
    possible = set(
        [
            index + 1,  # right
            index - 1,  # left
            index + size["width"],  # down
            index - size["width"],  # up
            index + size["width"] + 1,  # down right
            index + size["width"] - 1,  # down left
            index - size["width"] + 1,  # up right
            index - size["width"] - 1,  # up left
        ]
    )

    # if the index is on the left, remove left, up left and down left
    if index % size["width"] == 0:
        possible.remove(index - 1)
        possible.remove(index - size["width"] - 1)
        possible.remove(index + size["width"] - 1)
    # if the index is on the right, remove right, up right and down right
    elif index % size["width"] == size["width"] - 1:
        possible.remove(index + 1)
        possible.remove(index - size["width"] + 1)
        possible.remove(index + size["width"] + 1)

    # Remove impossible indexes
    possible = filter(lambda x: x >= 0 and x < size["total"], possible)

    return set(possible)


def solve(data, size):
    solution = 0

    number_chars = set([".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])

    for found_number in re.finditer(r"\d+", data):
        number = int(found_number.group())
        position = found_number.start(), found_number.end()

        is_serial = False
        for i in range(position[0], position[-1]):
            new_adjacent = find_adjacent_index(i, size)
            for index in new_adjacent:
                if data[index] not in number_chars:
                    is_serial = True
                    break

            if is_serial:
                break

        if is_serial:
            solution += number

    return solution


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data, size = parse(file)

    return solve(data, size)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

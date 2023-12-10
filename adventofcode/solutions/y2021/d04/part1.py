import os
import cProfile
import pstats

from functools import reduce

import numpy


def parse(data):
    winning_numbers = [int(n) for n in data[0].split(",")]
    data = data[2:]

    grids = []
    new_grid = []

    for line in data:
        if line == "":
            grids.append(new_grid)
            new_grid = []
        else:
            new_grid.append(
                [
                    {"found": False, "value": int(number)}
                    for number in list(filter(None, line.split(" ")))
                ]
            )

    grids.append(new_grid)

    return winning_numbers, grids


def check_number(grid, number):
    for line in grid:
        for current_number in filter(
            lambda n: (not n["found"]) and (n["value"] == number), line
        ):
            current_number["found"] = True


def _verify(grid):
    for line in grid:
        verify_line = reduce(lambda a, b: a and b, map(lambda n: n["found"], line))
        if verify_line:
            return True

    return False


def verify(grid):
    if _verify(grid):
        return "line"

    if _verify(numpy.transpose(grid)):
        return "column"

    return None


def calculate_solution(winning_number, orientation, grid):
    if orientation == "column":
        grid = numpy.transpose(grid)

    first_sum = reduce(
        lambda a, b: a + b,
        map(
            lambda line: reduce(
                lambda a, b: a + b,
                map(lambda n: n["value"] if not n["found"] else 0, line),
            ),
            grid,
        ),
    )

    return first_sum * winning_number


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        winning_numbers, grids = parse([line.strip() for line in file])

    winning_grid = None
    winning_number = None
    for winning_number in winning_numbers:
        for grid in grids:
            check_number(grid, winning_number)
            result = verify(grid)
            if result is not None:
                winning_grid = grid
                break

        if winning_grid is not None:
            break

    return calculate_solution(winning_number, result, winning_grid)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

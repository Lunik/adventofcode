import os
import cProfile
import pstats

from functools import reduce

from adventofcode.solutions.y2021.d09.part1 import parse, get_neighbour


def found_basin(position, already_checked, grid, grid_size):
    if position in already_checked:
        return None

    already_checked.add(position)

    if int(grid[position[0]][position[1]]) != 9:
        basin = [position]
        for neighbour_position in get_neighbour(position):
            if (
                neighbour_position in already_checked
                or neighbour_position[0] == -1
                or neighbour_position[1] == -1
                or neighbour_position[0] == grid_size[0]
                or neighbour_position[1] == grid_size[1]
            ):
                continue

            neighbour_basin = found_basin(
                neighbour_position, already_checked, grid, grid_size
            )
            if neighbour_basin:
                basin += neighbour_basin
        return basin

    return None


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        grid = parse(file)

    basins = []

    grid_size = (len(grid), len(grid[0]))

    already_checked = set()

    for pos_y, line in enumerate(grid):
        for pos_x, _ in enumerate(line):
            basin = found_basin((pos_y, pos_x), already_checked, grid, grid_size)
            if basin:
                basin = set(basin)
                if basin not in basins:
                    basins.append(basin)

    max_3 = [0, 0, 0]
    for basin in basins:
        length = len(basin)
        min_max = min(max_3)
        if length > min_max:
            max_3.remove(min_max)
            max_3.append(length)

    return reduce(lambda a, b: a * b, max_3)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

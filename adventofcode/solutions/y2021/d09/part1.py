import os
import cProfile
import pstats


def parse(file):
    return [list(line.rstrip("\n")) for line in file]


def debug_grid(grid):
    for line in grid:
        print(" ".join(line))


def get_neighbour(position):
    return [
        (position[0] - 1, position[1]),
        (position[0] + 1, position[1]),
        (position[0], position[1] - 1),
        (position[0], position[1] + 1),
    ]


def is_lower(position, grid):
    res = True

    for pos_y, pos_x in get_neighbour(position):
        try:
            if pos_y == -1 or pos_x == -1:
                raise IndexError
            neighbour = grid[pos_y][pos_x]
            res = res and (int(grid[position[0]][position[1]]) < int(neighbour))
        except IndexError:
            continue

    return res


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        grid = parse(file)

    lower_positions = []

    for pos_y, line in enumerate(grid):
        for pos_x, value in enumerate(line):
            position = (pos_y, pos_x)
            if is_lower(position, grid):
                lower_positions.append((position, int(value)))

    return sum([1 + pos[1] for pos in lower_positions])


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

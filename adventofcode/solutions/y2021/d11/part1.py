import os
import cProfile
import pstats


def parse(file):
    data = []

    for line in file:
        data.append([int(x) for x in line.strip("\n")])

    return data


def print_grid(grid):
    for line in grid:
        print(" ".join([str(x) for x in line]))


def charge_octopus(grid):
    for idy, line in enumerate(grid):
        for idx, _ in enumerate(line):
            grid[idy][idx] += 1

    return grid


def get_neighbors(position, max_height, max_width):
    neighbors = [
        (position[0] - 1, position[1] - 1),
        (position[0] - 1, position[1]),
        (position[0] - 1, position[1] + 1),
        (position[0], position[1] - 1),
        (position[0], position[1] + 1),
        (position[0] + 1, position[1] - 1),
        (position[0] + 1, position[1]),
        (position[0] + 1, position[1] + 1),
    ]

    return list(
        filter(
            lambda n: n[0] >= 0
            and n[0] < max_height
            and n[1] >= 0
            and n[1] < max_width,
            neighbors,
        )
    )


def flash_octopus(position, grid):
    neighbors = get_neighbors(position, len(grid), len(grid[0]))
    for neighbor in neighbors:
        grid[neighbor[0]][neighbor[1]] += 1


def is_waiting_to_flash(grid, has_flashed):
    for idy, line in enumerate(grid):
        for idx, octopus in enumerate(line):
            position = (idy, idx)
            if octopus > 9 and position not in has_flashed:
                return True

    return False


def resolve_loop(grid):
    charge_octopus(grid)

    has_flashed = []

    total_flash = 0

    while is_waiting_to_flash(grid, has_flashed):
        for idy, line in enumerate(grid):
            for idx, octopus in enumerate(line):
                position = (idy, idx)
                if octopus > 9 and position not in has_flashed:
                    total_flash += 1
                    has_flashed.append(position)
                    flash_octopus(position, grid)

    for idy, line in enumerate(grid):
        for idx, octopus in enumerate(line):
            if octopus > 9:
                grid[idy][idx] = 0

    return total_flash


def resolve(grid, steps):
    total_flash = 0

    for _ in range(steps):
        total_flash += resolve_loop(grid)

    return total_flash


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        grid = parse(file)

    return resolve(grid, 100)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

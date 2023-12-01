import os
import cProfile
import pstats


def parse(line):
    action, value = line.split(" ")
    return action, int(value)


def navigate(position, line):
    action, value = parse(line)

    if action == "forward":
        position[0] += value
    else:
        if action == "down":
            position[1] += value
        else:
            position[1] -= value

    return position


def main():
    # horizontal, depth
    position = [0, 0]

    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        for line in file:
            position = navigate(position, line)

    return position[0] * position[1]


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

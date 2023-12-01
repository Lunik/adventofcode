import os
import cProfile
import pstats


def parse(file):
    return file.read().strip("\n")


def solve(data, padding):
    cursor = 0
    end = cursor + padding
    while end < len(data):
        chunk = data[cursor:end]

        if len(chunk) == len(set(chunk)):
            break

        cursor += 1
        end = cursor + padding

    return end


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    return solve(data, 4)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

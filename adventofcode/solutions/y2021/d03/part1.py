import os
import cProfile
import pstats


def main():
    data = []

    index = 0
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = list(file.readline()[:-1])
        for index, line in enumerate(file):
            data = [int(l1) + int(l2) for l1, l2 in zip(data, list(line))]

    length = index + 2

    gamma_rate = []
    epsilon_rate = []
    for i in list(data):
        gamma_rate.append("1" if i / length > 0.5 else "0")
        epsilon_rate.append("0" if i / length > 0.5 else "1")

    result = int("".join(gamma_rate), 2) * int("".join(epsilon_rate), 2)

    return result


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

import os
import cProfile
import pstats


def parse(file):
    data = []

    for line in file:
        data.append([int(x) for x in line.strip("\n").split(" ")])

    return data


def is_all_zero(sequence):
    for number in sequence:
        if number != 0:
            return False

    return True


def solve(data):
    solution = 0

    for sequence in data:
        subsequences = [sequence]
        while not is_all_zero(subsequences[-1]):
            last_subsequence = subsequences[-1]
            new_subsequences = []

            for index, number in enumerate(last_subsequence):
                if index == 0:
                    continue
                new_subsequences.append(number - last_subsequence[index - 1])

            subsequences.append(new_subsequences)

        subsequences = list(reversed(subsequences))
        for index, subsequence in enumerate(subsequences):
            if index == 0:
                continue

            subsequence.append(subsequences[index - 1][-1] + subsequence[-1])

        solution += subsequences[-1][-1]

    return solution


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    return solve(data)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

import os
import cProfile
import pstats
import re


def parse(file):
    races = []

    times = re.findall(r"\d+", file.readline())
    distance = re.findall(r"\d+", file.readline())

    for i in range(len(times)):
        races.append({"time": int(times[i]), "max_distance": int(distance[i])})

    return races


def solve(races):
    solution = 1

    for race in races:
        for hold_time in range(1, race["time"]):
            left_time = race["time"] - hold_time
            distance_made = left_time * hold_time
            if distance_made >= race["max_distance"]:
                first_win = hold_time
                break

        for hold_time in range(race["time"] - 1, 0, -1):
            left_time = race["time"] - hold_time
            distance_made = left_time * hold_time
            if distance_made >= race["max_distance"]:
                last_win = hold_time
                break

        solution *= (last_win - first_win) + 1

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

import os
import cProfile
import pstats
from copy import deepcopy
from queue import PriorityQueue
import math
from collections import defaultdict


def parse(file):
    matrix = []

    for line in file:
        matrix.append(list(map(int, line.strip("\n"))))

    return matrix


def print_matrix(matrix):
    m = deepcopy(matrix)

    for line in m:
        print("".join(map(str, line)))


def get_neighbors(pos, maxs):
    neighbors = list(
        filter(
            lambda p: (p[0] >= 0 and p[0] < maxs[0]) and (p[1] >= 0 and p[1] < maxs[1]),
            [
                (pos[0] - 1, pos[1]),
                (pos[0], pos[1] - 1),
                (pos[0] + 1, pos[1]),
                (pos[0], pos[1] + 1),
            ],
        )
    )

    return neighbors


def find_path(matrix):
    size = (len(matrix), len(matrix[0]))
    end = (size[0] - 1, size[1] - 1)

    # Dictionary containing all case minimum risk to get there
    # In key, the case coordinates
    # In value, the minimal risk found to get there
    distances = defaultdict(lambda: math.inf, {(0, 0): 0})

    # Priority queue to first handle smaller risk value
    q = PriorityQueue()
    q.put((0, (0, (0, 0))))

    while q.qsize() > 0:
        _, case = q.get()

        # Reached the end
        if case[1] == end:
            return case[0]

        # Loop on all the neighbors
        for neighbor in get_neighbors(case[1], size):
            # Calculate new risk
            new_path_risk_level = case[0] + matrix[neighbor[0]][neighbor[1]]

            # If we have found a new path to a case that have a smaller risk value
            if new_path_risk_level < distances[neighbor]:
                # Store the new risk value to get to this case
                distances[neighbor] = new_path_risk_level
                # Put the neighboor in the handle queue
                q.put((new_path_risk_level, (new_path_risk_level, neighbor)))


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    return find_path(data)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

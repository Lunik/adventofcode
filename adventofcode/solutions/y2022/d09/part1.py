import os
import cProfile
import pstats
import math


def parse(file):
    instructions = []

    for line in file:
        line = line.strip("\n")
        direction, value = line.split(" ")
        instructions.append((direction, int(value)))

    return instructions


def sum_tuple(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def minus_tuple(t1, t2):
    return (t1[0] - t2[0], t1[1] - t2[1])


MOVES = dict(
    R=(1, 0),
    L=(-1, 0),
    U=(0, 1),
    D=(0, -1),
)


def solve(instructions, snake_length=2):
    snake = [(0, 0)] * snake_length

    visited_positions = set()

    for instruction in instructions:
        for interation in range(instruction[1]):
            snake[0] = sum_tuple(snake[0], MOVES[instruction[0]])
            for snake_part in range(1, len(snake)):
                dist = minus_tuple(snake[snake_part - 1], snake[snake_part])
                abs_dist = tuple(map(abs, dist))

                if max(abs_dist) > 1:
                    if dist[0] == 0:
                        snake[snake_part] = sum_tuple(
                            snake[snake_part], (0, -1 if dist[1] < 0 else 1)
                        )
                    elif dist[1] == 0:
                        snake[snake_part] = sum_tuple(
                            snake[snake_part], (-1 if dist[0] < 0 else 1, 0)
                        )
                    else:
                        snake[snake_part] = sum_tuple(
                            snake[snake_part],
                            (-1 if dist[0] < 0 else 1, -1 if dist[1] < 0 else 1),
                        )

            visited_positions.add(snake[-1])

    return len(visited_positions)


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

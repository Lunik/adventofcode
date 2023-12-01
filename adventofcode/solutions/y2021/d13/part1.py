import os
import cProfile
import pstats


def parse(file):
    points = []
    is_fold_instruction = False
    fold_instructions = []
    for line in file:
        line = line.strip("\n")
        if len(line) == 0:
            is_fold_instruction = True
            continue

        if is_fold_instruction:
            instruction = line.split(" ")[2].split("=")
            fold_instructions.append((instruction[0], int(instruction[1])))
        else:
            x, y = map(int, line.split(","))

            points.append((x, y))

    size_x = max(map(lambda m: m[0], points))
    size_y = max(map(lambda m: m[1], points))

    size_y += 2  # WHY ???

    matrix = [[0] * (size_x + 1) for i in range(size_y + 1)]

    for x, y in points:
        matrix[y][x] = 1

    return matrix, fold_instructions


def fold(matrix, line, value):
    if line == "x":
        new_matrix = []
        for line in matrix:
            left = line[0:value]
            right = line[value + 1 :]

            right.reverse()

            new_matrix.append(list(map(max, [t for t in zip(left, right)])))

    if line == "y":
        up = matrix[0:value]
        down = matrix[value + 1 :]

        down.reverse()

        new_matrix = [list(map(max, zip(*t))) for t in zip(up, down)]

    return new_matrix


def print_matrix(matrix):
    for line in matrix:
        print("".join(["#" if x else " " for x in line]))


def count_dots(matrix):
    return sum(map(sum, matrix))


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        matrix, fold_instructions = parse(file)

    line, value = fold_instructions[0]
    matrix = fold(matrix, line, value)

    return count_dots(matrix)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

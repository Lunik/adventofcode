import os

# y
# ^
# |
# |
# l______> x


def print_map(the_map):
    count = 0
    for line in the_map:
        print(count, "".join(line) + "".join(line))
        count += 1


def parse_line(line):
    return line.strip()


def is_tree(case):
    return case == "#"


def verify(the_map, moves):  # moves = (x, y)
    map_height = len(the_map)
    map_width = len(the_map[0])
    position = (0, 0)  # (x, y)

    count_tree = 0

    position = (position[0] + moves[0], position[1] + moves[1])

    while position[1] < map_height:
        case = the_map[position[1]][position[0] % map_width]

        if is_tree(case):
            count_tree += 1

        position = (position[0] + moves[0], position[1] + moves[1])

    return count_tree


def main():
    the_map = []

    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        for line in file:
            the_map.append(parse_line(line))

    # print_map(the_map)
    return verify(the_map, (3, 1))


if __name__ == "__main__":
    print(main())

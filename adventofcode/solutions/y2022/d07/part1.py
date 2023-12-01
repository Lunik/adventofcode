import os
import cProfile
import pstats


def parse(file):
    # - Type 'd' or 'f'
    # - Name
    # - Size int or 'None' if not calculed
    # - List of children if 'd', None if 'f'
    # - Parent None if root
    tree = ["d", "/", None, [], None]
    cursor = tree

    for line in file:
        line = line.strip("\n")

        if line[0] == "$":
            args = line.split(" ")
            command = args[1]
            if command == "cd":
                arg = args[2]
                if arg == "/":
                    cursor = tree
                elif arg == "..":
                    cursor = cursor[4]
                else:
                    child = list(filter(lambda child: child[1] == arg, cursor[3]))[0]
                    cursor = child

            elif command == "ls":
                continue

        else:
            args = line.split(" ")

            if args[0] == "dir":
                file = ["d", args[1], None, [], cursor]
            else:
                file = ["f", args[1], int(args[0]), None, cursor]

            cursor[3].append(file)

    return tree


def print_tree(tree, prof=0):
    print("  " * prof, tree[1], tree[2])
    if tree[0] == "d":
        for child in tree[3]:
            print_tree(child, prof + 1)


def get_size(tree):
    if tree[0] == "f":
        return tree[2]

    total = 0
    for child in tree[3]:
        total += get_size(child)

    tree[2] = total

    return total


def solve(tree, thresold):
    total = 0

    if tree[0] == "d":
        if tree[2] < thresold:
            total += tree[2]

        for child in tree[3]:
            total += solve(child, thresold)

    return total


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    get_size(data)

    return solve(data, 100000)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

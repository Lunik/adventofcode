import os
import cProfile
import pstats
import re

numbers = re.compile(r"\d+")


def parse(file):
    cards = []

    for line in file:
        _, card = line.strip().split(":")
        list_1, list_2 = card.split(" | ")
        card = (set(numbers.findall(list_1)), set(numbers.findall(list_2)))
        cards.append(card)

    return cards


def solve(cards):
    solution = 0

    for card in cards:
        intersection = card[0].intersection(card[1])

        count = len(intersection)
        if count > 0:
            solution += 1 * pow(2, count - 1)

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

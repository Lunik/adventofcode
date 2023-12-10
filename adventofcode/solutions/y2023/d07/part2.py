import os
import cProfile
import pstats
import re

from adventofcode.solutions.y2023.d07.part1 import solve, find_hand_type

hands_types = [
    {"name": "Five of a kind", "regex": r"(\w)(\1|J){4}"},
    {"name": "Four of a kind", "regex": r"(\w)(\1|J){3}"},
    {"name": "Full house", "regex": r"(\w)(\1|J){2}(\w)(\3|J)|(\w)(\5|J)(\w)(\7|J){2}"},
    {"name": "Three of a kind", "regex": r"(\w)(\1|J){2}"},
    {"name": "Two pairs", "regex": r"(\w)(\1|J)(\w)(\3|J)|(\w)(\5|J).(\w)(\4|J)"},
    {"name": "One pair", "regex": r"(\w)(\1|J)"},
    {"name": "High card", "regex": r".*"},
]

hands_types_values = [ht.get("name") for ht in hands_types]

cards_values = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def get_hand_from(cards, bid):
    return {
        "bid": bid,
        "cards": cards,
        "sorted_cards": "".join(sorted(cards, key=lambda x: cards_values.index(x))),
        "cards_sort_value": "".join(
            ["{:02d}".format(cards_values.index(c)) for c in cards]
        ),
    }


def parse(file):
    hands = []

    for line in file:
        cards, bid = line.strip("\n").split(" ")
        hands.append(get_hand_from(cards, bid))

    return hands


def find_hand_type_alt(initial_hand):
    if "J" not in initial_hand["cards"]:
        return find_hand_type(initial_hand)

    alt_hands = []

    all_chars = set(list(initial_hand["cards"]))
    all_chars.remove("J")
    if len(all_chars) == 0:
        all_chars = [cards_values[0]]

    for char in all_chars:
        new_alt_hand = get_hand_from(
            initial_hand["cards"].replace("J", char), initial_hand["bid"]
        )
        alt_hands.append(new_alt_hand)

    best_alt_hand = alt_hands[0]

    for alt_hand in alt_hands:
        find_hand_type(alt_hand)
        if hands_types_values.index(alt_hand["hand_type"]) <= hands_types_values.index(
            best_alt_hand["hand_type"]
        ):
            best_alt_hand = alt_hand

    initial_hand["hand_type"] = best_alt_hand["hand_type"]


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    return solve(data, find_hand_type=find_hand_type_alt)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

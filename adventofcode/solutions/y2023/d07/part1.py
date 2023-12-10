import os
import cProfile
import pstats
import re

hands_types = [
    {"name": "Five of a kind", "regex": r"(\w)\1{4}"},
    {"name": "Four of a kind", "regex": r"(\w)\1{3}"},
    {"name": "Full house", "regex": r"(\w)\1{2}(\w)\2|(\w)\3(\w)\4{2}"},
    {"name": "Three of a kind", "regex": r"(\w)\1{2}"},
    {"name": "Two pairs", "regex": r"(\w)\1(\w)\2|(\w)\3.(\w)\4"},
    {"name": "One pair", "regex": r"(\w)\1"},
    {"name": "High card", "regex": r".*"},
]

hands_types_values = [ht.get("name") for ht in hands_types]

cards_values = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


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


def find_hand_type(hand):
    cards = hand["cards"]
    sorted_cards = hand["sorted_cards"]

    current_hand_type = None

    for hand_type in hands_types:
        if re.search(hand_type["regex"], sorted_cards):
            current_hand_type = hand_type["name"]
            break

    hand["hand_type"] = current_hand_type


def solve(hands, find_hand_type):
    solution = 0

    for hand in hands:
        find_hand_type(hand)
        hand["highest_card"] = hand["sorted_cards"][0]
        hand["hand_type_sort_value"] = "{:02d}".format(
            hands_types_values.index(hand["hand_type"])
        )

    sorted_hands = sorted(
        hands,
        key=lambda x: x["hand_type_sort_value"] + x["cards_sort_value"],
        reverse=True,
    )

    for index, hand in enumerate(sorted_hands):
        solution += (index + 1) * int(hand["bid"])

    return solution


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    return solve(data, find_hand_type)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

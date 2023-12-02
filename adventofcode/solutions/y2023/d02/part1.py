import os
import cProfile
import pstats
import re
from collections import defaultdict

game_number_regex = re.compile(r"Game (\d+)")
turn_regex = re.compile(r"(\d+) (\w+)")

available_colors = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def parse_game(line):
    raw_game, raw_turns = line.split(":")
    game_number = game_number_regex.match(raw_game).group(1)

    turns = []
    for turn in raw_turns.split(";"):
        turns.append(turn_regex.findall(turn))

    return {
        "game_number": game_number,
        "turns": turns,
    }


def parse(file):
    games = []
    for line in file:
        games.append(parse_game(line.strip()))

    return games


def construct_viewed(game):
    game["viewed"] = defaultdict(int)
    for turn in game["turns"]:
        for hand in turn:
            color = hand[1]
            count = int(hand[0])
            if count > game["viewed"][color]:
                game["viewed"][color] = count


def solve(games, available_colors):
    solution = 0

    for game in games:
        game_is_possible = True
        construct_viewed(game)

        for color_name, color_count in available_colors.items():
            if color_count < game["viewed"][color_name]:
                game_is_possible = False
                break

        if game_is_possible:
            solution += int(game["game_number"])

    return solution


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    return solve(data, available_colors)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

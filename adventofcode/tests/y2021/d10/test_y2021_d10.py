from adventofcode.tests.utils.bench import calculate_duration

from adventofcode.solutions.y2021.d10.part1 import main as mainPart1
from adventofcode.solutions.y2021.d10.part2 import main as mainPart2


def test_part1():
    assert calculate_duration(mainPart1) == 339477


def test_part2():
    assert calculate_duration(mainPart2) == 3049320156

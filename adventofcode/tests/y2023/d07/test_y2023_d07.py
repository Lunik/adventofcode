from adventofcode.tests.utils.bench import calculate_duration

from adventofcode.solutions.y2023.d07.part1 import main as mainPart1
from adventofcode.solutions.y2023.d07.part2 import main as mainPart2


def test_part1():
    assert calculate_duration(mainPart1) == 248836197


def test_part2():
    assert calculate_duration(mainPart2) == 251195607

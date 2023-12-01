from adventofcode.tests.utils.bench import calculate_duration

from adventofcode.solutions.y2020.d14.part1 import main as mainPart1
from adventofcode.solutions.y2020.d14.part2 import main as mainPart2


def test_part1():
    assert calculate_duration(mainPart1) == 6631883285184


def test_part2():
    assert calculate_duration(mainPart2) == 3161838538691

from adventofcode.tests.utils.bench import calculate_duration

from adventofcode.solutions.y2022.d02.part1 import main as mainPart1
from adventofcode.solutions.y2022.d02.part2 import main as mainPart2


def test_part1():
    assert calculate_duration(mainPart1) == 11150


def test_part2():
    assert calculate_duration(mainPart2) == 8295

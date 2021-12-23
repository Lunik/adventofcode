from adventofcode.tests.utils.bench import calculate_duration

from adventofcode.solutions.y2021.d08.part1 import main as mainPart1
from adventofcode.solutions.y2021.d08.part2 import main as mainPart2


def test_part1():
  assert calculate_duration(mainPart1) == 369


def test_part2():
  assert calculate_duration(mainPart2) == 1031553

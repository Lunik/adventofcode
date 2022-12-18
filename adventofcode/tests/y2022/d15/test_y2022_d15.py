from adventofcode.tests.utils.bench import calculate_duration

from adventofcode.solutions.y2022.d15.part1 import main as mainPart1
from adventofcode.solutions.y2022.d15.part2 import main as mainPart2


def test_part1():
  assert calculate_duration(mainPart1) == 4502208


def test_part2():
  assert calculate_duration(mainPart2) == 13784551204480

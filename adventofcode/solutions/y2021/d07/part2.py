import os
import cProfile
import pstats

from adventofcode.solutions.y2021.d07.part1 import parse, align


def fuel_calculator(hight, target):
  diff = abs(hight-target)
  return diff*(diff+1)/2


def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    data = file.read()

  crabs = parse(data)

  fuel, _ = align(fuel_calculator, crabs)

  return int(fuel)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

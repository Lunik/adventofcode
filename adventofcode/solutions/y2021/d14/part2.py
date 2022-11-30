import os
import cProfile
import pstats
import time

from adventofcode.solutions.y2021.d14.part1 import parse, loop

def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    molecule, formulas = parse(file)

  return loop(molecule, formulas, 40)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

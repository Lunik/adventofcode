import os
import cProfile
import pstats

from adventofcode.solutions.y2021.d13.part1 import parse, fold, count_dots, print_matrix

def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    matrix, fold_instructions = parse(file)

  for line, value in fold_instructions:
    matrix = fold(matrix, line, value)

  print("")
  print_matrix(matrix)

  return matrix


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

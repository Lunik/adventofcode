import os
import cProfile
import pstats

from adventofcode.solutions.y2022.d08.part1 import parse

def solve(matrix):
  max_seable_trees = 0

  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      left = matrix[i][:j]
      right = matrix[i][j+1:]
      top = [c[j] for c in matrix[:i]]
      bottom = [c[j] for c in matrix[i+1:]]

      seable_trees = 1
      lines = [reversed(left), right, reversed(top), bottom]
      for line in lines:
        line_seable_trees = 0
        for idx, x in enumerate(line):
          line_seable_trees += 1
          if x >= matrix[i][j]:
            break

        seable_trees = seable_trees * line_seable_trees

      max_seable_trees = max(seable_trees, max_seable_trees)

  return max_seable_trees

def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    data = parse(file)

  return solve(data)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

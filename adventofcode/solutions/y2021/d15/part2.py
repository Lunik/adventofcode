import os
import cProfile
import pstats

from adventofcode.solutions.y2021.d15.part1 import find_path, print_matrix

def parse(file):
  matrix = []

  for line in file:
    matrix.append(list(map(int, line.strip('\n'))))

  new_matrix = []

  for i in range(5):
    for line in matrix:
      new_line = []
      for j in range(5):
        new_line = new_line + list(map(lambda x: ((x-1+i+j)%9)+1, line))

      new_matrix.append(new_line)

  return new_matrix

def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    data = parse(file)

  return find_path(data)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

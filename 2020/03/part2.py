from functools import reduce
from part1 import parseLine, verify

if __name__ == "__main__":
  the_map = []

  with open('input.txt', 'r') as f:
    for line in f:
      the_map.append(parseLine(line))

  trees_count = []
  for move in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    trees_count.append(verify(the_map, move))

  print(reduce(lambda a, b: a*b, trees_count))

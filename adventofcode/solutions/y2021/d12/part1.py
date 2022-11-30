import os
import cProfile
import pstats
import re
from copy import copy

def parse(file):
  cave = dict()

  for line in file:
    path_from, path_to = line.strip('\n').split('-')

    if path_from not in cave:
      cave[path_from] = []

    if path_to not in cave:
      cave[path_to] = []

    cave[path_from].append(path_to)
    cave[path_to].append(path_from)

  return cave

def debug_cave(cave):
  for node, neighbors in cave.items():
    print(node, neighbors)

def find_path(cave, node="start", path=[]):
  p = copy(path)
  p.append(node)

  results = []

  for neighbors in cave[node]:
    # Found the end, Stop and save the path
    if neighbors == "end":
      p2 = copy(p)
      p2.append(neighbors)
      results.append(p2)
      continue

    if neighbors in p:
      # Already walked cave
      if re.match(r'[A-Z]+', neighbors):
        # It's large cave, continue exploring
        res1 = find_path(cave, neighbors, p)
        for res in res1:
          # Save all found path
          results.append(res)
      else:
        # It's a small cave
        # Dead end, Abort
        continue
    else:
      # New cave, continue exploring
      res2 = find_path(cave, neighbors, p)
      for res in res2:
          # Save all found path
        results.append(res)

  return results


def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    cave = parse(file)

  #debug_cave(cave)

  res = find_path(cave)

  return len(res)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

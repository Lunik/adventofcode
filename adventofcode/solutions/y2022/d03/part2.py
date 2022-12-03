import os
import cProfile
import pstats

from adventofcode.solutions.y2022.d03.part1 import parse, PRIORITIES

def solve(bags):
  group = []
  score = 0

  for bag in bags:
    group.append(bag)

    if len(group) == 3:
      bag1 = set(''.join(group[0]))
      bag2 = set(''.join(group[1]))
      bag3 = set(''.join(group[2]))

      intersection = list(bag1.intersection(bag2).intersection(bag3))

      score += PRIORITIES.index(intersection[0])

      group = []

  return score

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

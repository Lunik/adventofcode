import os
import cProfile
import pstats

def parse(data):
  return [int(c) for c in data.split(',')]


def fuel_calculator(hight, target):
  return abs(hight-target)


def align(fuel_calculator_function, crabs):
  higher = max(crabs)
  lower = min(crabs)

  min_alignment = (100000000000000000000000000, -1)

  for i in range(lower, higher+1):
    res = sum(map(fuel_calculator_function, crabs, [i]*len(crabs)))
    if res < min_alignment[0]:
      min_alignment = (res, i)

  return min_alignment


def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    data = file.read()

  crabs = parse(data)

  fuel, _ = align(fuel_calculator, crabs)

  return fuel


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

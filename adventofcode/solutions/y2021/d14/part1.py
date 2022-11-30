import os
import cProfile
import pstats
import re
from collections import Counter
from copy import copy

def parse(file):
  formulas = dict()

  is_formula = False
  initial = None

  for line in file:
    line = line.strip('\n')

    if len(line) == 0:
      is_formula = True
      continue

    if is_formula:
      res = re.match(r'(\w\w)\s->\s(\w)', line)
      m = res.group(1)
      r = res.group(2)
      formulas[m] = [m[0] + r, r + m[1]]
    else:
      initial = line

  return initial, formulas

def calc(counts, formulas):
  result = Counter()

  for pair, count in counts.items():
    for new_pair in formulas[pair]:
      result[new_pair] += counts[pair]

  return result

def loop(molecule, formulas, count):
  counts = Counter()
  for i in range(len(molecule)-1):
    counts[molecule[i:i+2]] += 1

  for i in range(count):
    counts = calc(counts, formulas)

  res = Counter()
  for count, value in counts.items():
    res[count[0]] += value

  res[molecule[-1]] += 1

  res = [v for _, v in res.items()]

  return max(res) - min(res)

def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    molecule, formulas = parse(file)

  return loop(molecule, formulas, 10)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

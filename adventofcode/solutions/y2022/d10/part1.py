import os
import cProfile
import pstats
import re

def parse(file):
  instructions = []

  for line in file:
    res = re.match(r'(\w+)(\s(-?\d+))?', line.strip('\n'))

    op = res.group(1)
    arg = res.group(2)

    if arg:
      arg = int(arg)

    instructions.append((op, arg))

  return instructions

OP_CYCLES = dict(
  noop=1,
  addx=2,
)

def caclulate_strength(X, cycle):
  return X * cycle

def solve(instructions):
  X = 1
  cycle = 0
  signal_strength = None

  result = 0

  for op, arg in instructions:
    for i in range(OP_CYCLES[op]):
      cycle += 1
      if (cycle%40) == 20:
        signal_strength = caclulate_strength(X, cycle)
        result += signal_strength

    if op == 'addx':
      X += arg

  return result

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

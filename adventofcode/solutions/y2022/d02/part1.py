import os
import cProfile
import pstats

def parse(file):
  data = []

  for line in file:
    line = line.strip('\n')

    elf, me = line.split(' ')

    data.append((ord(elf) - 65, ord(me) - 23 - 65))

  return data

RULE = [2, 0, 1]

def solve(cheatsheet):
  score = 0

  for elf, me in cheatsheet:
    score += (me + 1)

    if elf == me:
      score += 3
    elif RULE[me] == elf:
      score += 6

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

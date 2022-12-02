import os
import cProfile
import pstats

def parse(file):
  elfs = []

  elf = []
  for line in file:
    line = line.strip('\n')

    if line == "":
      elfs.append(elf)
      elf = []
      continue

    elf.append(int(line))

  elfs.append(elf)

  return elfs

def solve(elfs):
  total = list(map(sum, elfs))

  max_value = max(total)

  return max_value

def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    elfs = parse(file)

  return solve(elfs)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

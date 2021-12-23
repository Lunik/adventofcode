import os
import cProfile
import pstats

def parse(file):
  sequences = []

  for line in file:
    splitted = line.rstrip('\n').split(' | ')
    sequences.append({
      'left': [''.join(sorted(string)) for string in splitted[0].split(' ')],
      'right': [''.join(sorted(string)) for string in splitted[1].split(' ')]
    })

  return sequences


def count_1_4_7_8(sub_sequence):
  length = len(sub_sequence)

  # 1, 4, 7, 8
  return int(length==2) + int(length==4) + int(length==3) + int(length==7)


def solve(sequences):
  total = 0

  for sequence in sequences:
    total += sum(map(count_1_4_7_8, sequence['right']))

  return total


def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    sequences = parse(file)

  return solve(sequences)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

from itertools import product

from part1 import findInvalidNumber

def findSumMatch(sum_count, sum_to_find, sequence):
  for start in range(0, len(sequence) - sum_count):
    subset_sequence = sequence[start:sum_count]
    if sum(subset_sequence) == sum_to_find:
      return subset_sequence

  return None

if __name__ == "__main__":

  encryption_offset = 25

  sequence = []

  with open('input.txt') as f:
    for line in f:
      sequence.append(int(line))

  invalid_number = findInvalidNumber(encryption_offset, sequence)

  sum_count = 2

  while sum_count <= len(sequence):
    result = findSumMatch(sum_count, invalid_number, sequence)

    if result is not None:
      break

    sum_count += 1

  print(max(result) + min(result))
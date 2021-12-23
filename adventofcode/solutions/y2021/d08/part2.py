import os
import cProfile
import pstats

from adventofcode.solutions.y2021.d08.part1 import parse

DIGITS_LENGTH = {
  1: None,
  2: 1,
  3: 7,
  4: 4,
  5: [2, 3, 5],
  6: [0, 6, 9],
  7: 8
}

def find_digits_string(digits, sequences):
  for string in sequences:
    length = len(string)
    if isinstance(DIGITS_LENGTH[length], int):
      digits[DIGITS_LENGTH[length]] = string
    else:
      if length == 5:
        # 3 have all segments of 1
        if digits[1] and all(letter in string for letter in digits[1]):
          digits[3] = string
        # 6 have all segments of 5
        elif digits[6] and all(letter in digits[6] for letter in string):
          digits[5] = string
        # 2 is the only remaining number is 3 and 5 are found
        elif string not in (digits[3], digits[5]):
          digits[2] = string

      if length == 6:
        # 6 have exactly one segment of 1
        if digits[1] and ((digits[1][0] in string) ^ (digits[1][1] in string)):
          digits[6] = string
        # 9 have all segments of 3
        elif digits[3] and all(letter in string for letter in digits[3]):
          digits[9] = string
        # 0 is the only remaining number is 6 and 9 are found
        elif string not in (digits[6], digits[9]):
          digits[0] = string


def solve(sequence):
  #print("solve ==>", sequence)
  digits = {
    0: None, 1: None, 2: None, 3: None, 4: None,
    5: None, 6: None, 7: None, 8: None, 9: None
  }

  sequences = {*sequence['left'], *sequence['right']}
  while sum([0 if v is None else 1 for v in digits.values()]) < len(sequences):
    find_digits_string(digits, sequences)

  reverse_digits = {v: k for k,v in digits.items()}

  result = ""
  for subsequence in sequence['right']:
    result += str(reverse_digits[subsequence])

  return int(result)


def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    sequences = parse(file)

  return sum([solve(sequence) for sequence in sequences])


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

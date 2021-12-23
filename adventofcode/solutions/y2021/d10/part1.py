import os
import cProfile
import pstats

PAIRING_CHAR = {
  ')': '(',
  '(': ')',
  ']': '[',
  '[': ']',
  '}': '{',
  '{': '}',
  '>': '<',
  '<': '>'
}

INVALID_CHAR_POINTS = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

class ExpectingChar(Exception):
  def __init__(self, message, char):
    super().__init__(message)

    self.char = char


def check_line(line):
  counter = ""
  # print(f"\nline: {line}")
  for char in list(line):
    if char in "({[<":
      counter += char
    elif char in ")}]>" and counter[-1] == PAIRING_CHAR[char]:
      counter = counter[:-1]
    else:
      raise ExpectingChar(f"Expected {PAIRING_CHAR[counter[-1]]}, but found {char} instead.", char)

  return True


def solve(line):
  try:
    check_line(line)
  except ExpectingChar as _:
    # print(_)
    return INVALID_CHAR_POINTS[_.char]

  # print("is valid")
  return 0


def main():
  total = 0
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    for line in file:
      total += solve(line.strip('\n'))

  return total


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

import os

from functools import reduce


def parse_groups(data):
  return map(
    # Map for each groups
    lambda g: reduce(
      # Calculate intersection of all answers by groups
      lambda a, b: set(a) & set(b),
      filter(
        # Removing empty line wich can distort intersection caclulation
        lambda r: r != '',
        g.split('\n'))),
    data.split('\n\n'))


def verify(groups):
  return reduce(
    # Add all length of groups sets (after intersections)
    lambda a, b: (a if isinstance(a, int) else len(a)) + len(b),
    groups)


def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    groups = parse_groups(file.read())

  return verify(groups)


if __name__ == "__main__":
  print(main())

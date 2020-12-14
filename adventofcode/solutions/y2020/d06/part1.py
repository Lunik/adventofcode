import os

from functools import reduce

def parse_groups(data):
  return map(lambda g: set(g.replace('\n', '')), data.split('\n\n'))

def verify(groups):
  return reduce(lambda a, b: (len(a) if isinstance(a, set) else a) + len(b), groups)

def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    groups = parse_groups(file.read())

  return verify(groups)

if __name__ == "__main__":
  print(main())

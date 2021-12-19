import os

from functools import reduce

from adventofcode.solutions.y2021.d05.part1 import calculate_line, parse


def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    vectors = parse(file.readlines())


  #vectors = filter(lambda v: v[0][0] == v[1][0] or v[0][1] == v[1][1], vectors)

  lines = reduce(lambda a, b: a + b, [calculate_line(vector) for vector in vectors])

  counter = {}
  for point in lines:
    if str(point) not in counter:
      counter[str(point)] = 0
    counter[str(point)] += 1

  result = reduce(lambda a, b: a + b, map(lambda v: int(v >= 2), counter.values()))

  return result


if __name__ == "__main__":
  print(main())

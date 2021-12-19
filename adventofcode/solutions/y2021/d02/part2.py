import os

from adventofcode.solutions.y2021.d02.part1 import parse


def navigate(position, line):
  action, value = parse(line)

  if action == "forward":
    position[0] += value
    position[1] += position[2] * value
  else:
    if action == "down":
      position[2] += value
    else:
      position[2] -= value

  return position


def main():
  # horizontal, depth, aim
  position = [0, 0, 0]

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    for line in file:
      position = navigate(position, line)

  return position[0] * position[1]


if __name__ == "__main__":
  print(main())

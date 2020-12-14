import os

from adventofcode.solutions.y2020.d05.part1 import parse_seat, get_seat_position

def print_plane(plane):
  count = 0
  print("\t", "0 1 2 3 4 5 6 7")
  for row in plane:
    print(count, '\t', ' '.join(row))
    count += 1

def main():
  plane = [['_' for colum in range(8)] for row in range(128)]

  positions = []

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    for line in file:
      seat = parse_seat(line)

      position = get_seat_position(seat)
      positions.append(position)

      plane[position[0]][position[1]] = "X"

  return plane

if __name__ == "__main__":
  print(main())

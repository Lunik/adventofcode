import os


from adventofcode.solutions.y2020.d05.part1 import parse_seat, get_seat_position, get_postion_id


def print_plane(plane):
  count = 0
  print("\t", "0 1 2 3 4 5 6 7")
  for row in plane:
    print(count, '\t', ' '.join(row))
    count += 1


def find_seat(plane):

  for row in range(1, 128):
    for column in range(1, 8):
      if plane[row][column] == '_' \
        and plane[row][column - 1] == 'X' \
        and plane[row][column + 1] == 'X':
        return (row, column)

  return None


def main():
  plane = [['_' for colum in range(8)] for row in range(128)]

  positions = []

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    for line in file:
      seat = parse_seat(line)

      position = get_seat_position(seat)
      positions.append(position)

      plane[position[0]][position[1]] = "X"

  seat_position = find_seat(plane)
  return get_postion_id(seat_position)


if __name__ == "__main__":
  print(main())

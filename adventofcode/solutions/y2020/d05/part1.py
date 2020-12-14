import re
import math
import os


def parse_seat(string):
  return re.match('([FB]{7})([LR]{3})', string).groups()


def get_range(actions, some_range):
  if len(actions) == 0:
    return some_range.start

  action = actions.pop()

  return_value = None

  if action in ["F", "L"]:
    return_value = get_range(actions, some_range[:math.ceil(len(some_range)/2)])
  elif action in ["B", "R"]:
    return_value = get_range(actions, some_range[math.ceil(len(some_range)/2):])

  return return_value


def get_seat_position(seat):
  row = get_range(list(seat[0][::-1]), range(128))
  column = get_range(list(seat[1][::-1]), range(8))

  return (row, column)


def get_postion_id(position):
  return (position[0] * 8) + position[1]


def main():
  seats_ids = []

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    for line in file:
      seat = parse_seat(line)

      position = get_seat_position(seat)

      seats_ids.append(get_postion_id(position))

  return max(seats_ids)


if __name__ == "__main__":
  print(main())

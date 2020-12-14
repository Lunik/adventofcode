import copy
import os

def parse_line(line):
  return list(line)

def print_waiting_room(waiting_room):
  for row in waiting_room:
    print(''.join(row))

def get_wr_size(waiting_room):
  return (len(waiting_room), len(waiting_room[0])) # y, x

def define_next_seat_state(pos_x, pos_y, waiting_room, wr_size):
  seat_status = waiting_room[pos_y][pos_x]
  if seat_status == ".":
    return (False, seat_status)

  occupied_neighbors = 0

  for delta_y in range(-1, 2):
    orig_new_y = pos_y + delta_y
    if orig_new_y < 0 or orig_new_y >= wr_size[0]:
      continue

    for delta_x in range(-1, 2):
      orig_new_x = pos_x + delta_x
      if orig_new_x < 0 or orig_new_x >= wr_size[1]:
        continue

      if orig_new_y == pos_y and orig_new_x == pos_x:
        continue

      test_case = waiting_room[orig_new_y][orig_new_x]

      if test_case == "#":
        occupied_neighbors += 1

  return_value = (False, seat_status)
  if seat_status == "L" and occupied_neighbors == 0:
    return_value = (True, "#")
  elif seat_status == "#" and occupied_neighbors >= 4:
    return_value =  (True, "L")

  return return_value

def count_seat(status, waiting_room, wr_size):

  count = 0

  for pos_y in range(wr_size[0]):
    for pos_x in range(wr_size[1]):
      if waiting_room[pos_y][pos_x] == status:
        count += 1

  return count


def resolve(waiting_room, funct):
  stable = False

  wr_size = get_wr_size(waiting_room)

  while not stable:
    new_wr = copy.deepcopy(waiting_room)
    stable = True
    for pos_y in range(wr_size[0]):
      for pos_x in range(wr_size[1]):
        changed, new_wr[pos_y][pos_x] = funct(pos_x, pos_y, waiting_room, wr_size)

        stable = stable & (not changed)

    waiting_room = new_wr

  return count_seat("#", waiting_room, wr_size)

def main():
  waiting_room = []

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    for line in file:
      waiting_room.append(parse_line(line.strip()))

  return resolve(waiting_room, define_next_seat_state)

if __name__ == "__main__":
  print(main())

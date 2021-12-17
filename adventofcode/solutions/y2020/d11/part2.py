import os


from adventofcode.solutions.y2020.d11.part1 import parse_line, resolve


def define_net_seat_state(pos_x, pos_y, waiting_room, wr_size):
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

      new_x = orig_new_x
      new_y = orig_new_y
      test_case = waiting_room[new_y][new_x]

      out = False
      while test_case == ".":
        new_y += delta_y
        new_x += delta_x
        if new_y < 0 or new_y >= wr_size[0]:
          out = True
          break
        if new_x < 0 or new_x >= wr_size[1]:
          out = True
          break

        test_case = waiting_room[new_y][new_x]

      if out:
        continue

      if test_case == "#":
        occupied_neighbors += 1

  return_value = (False, seat_status)
  if seat_status == "L" and occupied_neighbors == 0:
    return_value = (True, "#")
  elif seat_status == "#" and occupied_neighbors >= 5:
    return_value = (True, "L")

  return return_value


def main():
  waiting_room = []

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    for line in file:
      waiting_room.append(parse_line(line.strip()))

  return resolve(waiting_room, define_net_seat_state)


if __name__ == "__main__":
  print(main())

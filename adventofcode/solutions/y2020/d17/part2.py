import os


def parse_data(y_len, x_len, data):
  first_slice = []

  for _ in range(int((x_len - len(data.split('\n')))/2)):
    first_slice.append(['.' for x in range(y_len)])

  for line in data.split('\n'):
    x_dimension = ['.' for _ in range(int((x_len - len(list(line)))/2))] \
      + list(line) \
      + ['.' for _ in range(int((x_len - len(list(line)))/2))]

    first_slice.append(x_dimension)

  for _ in range(int((x_len - len(data.split('\n')))/2)):
    first_slice.append(['.' for x in range(y_len)])

  return first_slice


def print_dimension(dimension):
  for pos_w, dimension_w in enumerate(dimension):
    for pos_z, dimension_z in enumerate(dimension_w):
      print("w=", pos_w, "z=", pos_z)
      for _, dimension_y in enumerate(dimension_z):
        print(' '.join(dimension_y))


def find_neighbors(position, dimension):
  neighbors = []

  for pos_w in range(-1, 2):
    if position[0] + pos_w not in range(len(dimension)):
      continue
    for pos_z in range(-1, 2):
      if position[1] + pos_z not in range(len(dimension[pos_w])):
        continue
      for pos_y in range(-1, 2):
        if position[2] + pos_y not in range(len(dimension[pos_w][pos_z])):
          continue
        for pos_x in range(-1, 2):
          if position[3] + pos_x not in range(len(dimension[pos_w][pos_z][pos_y])):
            continue

          if pos_w == pos_z == pos_y == pos_x == 0:
            continue

          neighbors.append(
            dimension[position[0] + pos_w]\
            [position[1] + pos_z]\
            [position[2] + pos_y]\
            [position[3] + pos_x])

  return neighbors


def generate_dimension(size):
  return [[[
    ['.' for _ in range(size[3])]
      for _ in range(size[2])]
        for _ in range(size[1])]
          for _ in range(size[0])]


def evolve(size, dimension):
  new_dimension = generate_dimension(size)

  for pos_w, dimension_w in enumerate(dimension):
    for pos_z, dimension_z in enumerate(dimension_w):
      for pos_y, dimension_y in enumerate(dimension_z):
        for pos_x, _ in enumerate(dimension_y):
          neighbors = find_neighbors((pos_w, pos_z, pos_y, pos_x), dimension)
          active_neighbors = neighbors.count('#')

          if dimension[pos_w][pos_z][pos_y][pos_x] == "#":
            if active_neighbors not in [2, 3]:
              new_dimension[pos_w][pos_z][pos_y][pos_x] = '.'
            else:
              new_dimension[pos_w][pos_z][pos_y][pos_x] = dimension[pos_w][pos_z][pos_y][pos_x]

          else:
            if active_neighbors == 3:
              new_dimension[pos_w][pos_z][pos_y][pos_x] = '#'
            else:
              new_dimension[pos_w][pos_z][pos_y][pos_x] = dimension[pos_w][pos_z][pos_y][pos_x]

  return new_dimension


def count_active_cube(dimension):
  total = 0

  for _, dimension_w in enumerate(dimension):
    for _, dimension_z in enumerate(dimension_w):
      for _, dimension_y in enumerate(dimension_z):
        total += dimension_y.count('#')

  return total


def main():
  size = (20, 20, 20, 20)
  initial_dimension = generate_dimension(size)

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    initial_state = parse_data(size[1], size[2], file.read())

  initial_dimension[int(size[0]/2)][int(size[1]/2)] = initial_state

  new_dimension = initial_dimension

  for _ in range(6):
    new_dimension = evolve(size, new_dimension)

  return count_active_cube(new_dimension)


if __name__ == "__main__":
  print(main())


# y
# ^
# |
# |
# l______> x

def printMap(the_map):
  count = 0
  for line in the_map:
    print(count, ''.join(line) + ''.join(line))
    count += 1

def parseLine(line):
  return list(line.strip())

def isTree(case):
  return case == "#"

def verify(the_map, moves): # moves = (x, y)
  map_height = len(the_map)
  map_width = len(the_map[0])
  position = (0, 0) # (x, y)

  count_tree = 0

  position = (position[0] + moves[0], position[1] + moves[1])

  while position[1] < map_height:
    case = the_map[position[1]][position[0]%map_width]
    
    if isTree(case):
      count_tree += 1

    position = (position[0] + moves[0], position[1] + moves[1])

  return count_tree

if __name__ == "__main__":
  the_map = []

  with open('input.txt', 'r') as f:
    for line in f:
      the_map.append(parseLine(line))

  #printMap(the_map)
  print(verify(the_map, (3, 1)))

import copy

def parseLine(line):
  return list(line)

def printWaitingRoom(waiting_room):
  for row in waiting_room:
    print(''.join(row))

def getWRSize(waiting_room):
  return (len(waiting_room), len(waiting_room[0])) # y, x

def defineNextSeatState(posX, posY, waiting_room, wr_size):
  seat_status = waiting_room[posY][posX]
  if seat_status == ".":
    return (False, seat_status)

  occupied_neighbors = 0

  for deltaY in range(-1, 2):
    origNewY = posY + deltaY
    if origNewY < 0 or origNewY >= wr_size[0]:
      continue

    for deltaX in range(-1, 2):
      origNewX = posX + deltaX
      if origNewX < 0 or origNewX >= wr_size[1]:
        continue

      if origNewY == posY and origNewX == posX:
        continue

      test_case = waiting_room[origNewY][origNewX]

      if test_case == "#":
         occupied_neighbors += 1

  if seat_status == "L" and occupied_neighbors == 0:
    return (True, "#")
  elif seat_status == "#" and occupied_neighbors >= 4:
    return (True, "L")
  else:
    return (False, seat_status)

def countSeat(status, waiting_room, wr_size):

  count = 0

  for y in range(wr_size[0]):
    for x in range(wr_size[1]):
      if waiting_room[y][x] == status:
        count += 1

  return count


def resolve(waiting_room, defineNextSeatState):
  stable = False

  wr_size = getWRSize(waiting_room)

  while not stable:
    new_wr = copy.deepcopy(waiting_room)
    stable = True
    for y in range(wr_size[0]):
      for x in range(wr_size[1]):
        changed, new_wr[y][x] = defineNextSeatState(x, y, waiting_room, wr_size)

        stable = stable & (not changed)

    waiting_room = new_wr

  return countSeat("#", waiting_room, wr_size)

if __name__ == "__main__":

  waiting_room = []

  with open('input.txt', 'r') as f:
    for line in f:
      waiting_room.append(parseLine(line.strip()))

  print(resolve(waiting_room, defineNextSeatState))
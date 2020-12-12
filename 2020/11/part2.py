import copy

from part1 import parseLine, printWaitingRoom, getWRSize, countSeat, resolve

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

      newX = origNewX
      newY = origNewY
      test_case = waiting_room[newY][newX]

      out = False
      while test_case == ".":
        newY += deltaY
        newX += deltaX
        if newY < 0 or newY >= wr_size[0]:
          out = True
          break
        if newX < 0 or newX >= wr_size[1]:
          out = True
          break

        test_case = waiting_room[newY][newX]

      if out:
        continue

      if test_case == "#":
         occupied_neighbors += 1

  if seat_status == "L" and occupied_neighbors == 0:
    return (True, "#")
  elif seat_status == "#" and occupied_neighbors >= 5:
    return (True, "L")
  else:
    return (False, seat_status)

if __name__ == "__main__":

  waiting_room = []

  with open('input.txt', 'r') as f:
    for line in f:
      waiting_room.append(parseLine(line.strip()))

  print(resolve(waiting_room, defineNextSeatState))
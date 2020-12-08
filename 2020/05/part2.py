from part1 import parseSeat, getSeatPosition, getPostionId

def printPlane(plane):
  count = 0
  print("\t", "0 1 2 3 4 5 6 7")
  for row in plane:
    print(count, '\t', ' '.join(row))
    count += 1

if __name__ == "__main__":
  plane = [['_' for colum in range(8)] for row in range(128)]

  positions = []

  with open('input.txt', 'r') as f:
    for line in f:
      seat = parseSeat(line)

      position = getSeatPosition(seat)
      positions.append(position)

      plane[position[0]][position[1]] = "X"

  printPlane(plane)

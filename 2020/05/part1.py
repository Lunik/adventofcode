import re
import math

def parseSeat(string):
  return re.match('([FB]{7})([LR]{3})', string).groups()

def getRange(actions, rg):
  if len(actions) == 0:
    return rg.start

  action = actions.pop()

  if action in ["F", "L"]:
    return getRange(actions, rg[:math.ceil(len(rg)/2)])
  elif action in ["B", "R"]:
    return getRange(actions, rg[math.ceil(len(rg)/2):])

def getSeatPosition(seat):
  row = getRange(list(seat[0][::-1]), range(128))
  column = getRange(list(seat[1][::-1]), range(8))

  return (row, column)

def getPostionId(position):
  return (position[0] * 8) + position[1]

if __name__ == "__main__":
  seats_ids = []

  with open('input.txt', 'r') as f:
    for line in f:
      seat = parseSeat(line)

      position = getSeatPosition(seat)

      seats_ids.append(getPostionId(position))
      

  print(max(seats_ids))
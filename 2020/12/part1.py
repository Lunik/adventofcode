import re

def parseLine(line):
  groups = re.match('(\w)(\d+)', line).groups()

  return (groups[0], int(groups[1]))

class Boat:
  def __init__(self, orientation):
    self.orientation = orientation
    self.navigation = dict(
      N=0,
      E=0,
      S=0,
      W=0)

  def rotate(self, direction, angle):
    cardinals = list(self.navigation.keys())
    if direction == 'R':
      self.orientation = cardinals[int((cardinals.index(self.orientation) + (angle/90)) % len(cardinals))]
    else:
      self.orientation = cardinals[int((cardinals.index(self.orientation) - (angle/90)) % len(cardinals))]

  def execAction(self, action, value):
    if action in ['N', 'S', 'E', 'W']:
      self.navigation[action] += value

    elif action in ['R', 'L']:
      self.rotate(action, value)

    elif action == "F":
      self.navigation[self.orientation] += value

  def getDistance(self):
    return abs(self.navigation['N'] - self.navigation['S']) + \
      abs(self.navigation['E'] - self.navigation['W'])

  def debug(self):
    print(self.orientation, self.navigation)

if __name__ == "__main__":
  boat = Boat('E')

  with open('input.txt', 'r') as f:
    for line in f:
      action = parseLine(line.strip())
      boat.execAction(*action)

  print(boat.getDistance())
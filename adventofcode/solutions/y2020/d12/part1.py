import re
import os

def parse_line(line):
  groups = re.match('(\\w)(\\d+)', line).groups()

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
      self.orientation = cardinals[
        int((cardinals.index(self.orientation) + (angle/90)) % len(cardinals))
      ]
    else:
      self.orientation = cardinals[
        int((cardinals.index(self.orientation) - (angle/90)) % len(cardinals))
      ]

  def exec_action(self, action, value):
    if action in ['N', 'S', 'E', 'W']:
      self.navigation[action] += value

    elif action in ['R', 'L']:
      self.rotate(action, value)

    elif action == "F":
      self.navigation[self.orientation] += value

  def get_distance(self):
    return abs(self.navigation['N'] - self.navigation['S']) + \
      abs(self.navigation['E'] - self.navigation['W'])

  def debug(self):
    print(self.orientation, self.navigation)

def main():
  boat = Boat('E')

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    for line in file:
      action = parse_line(line.strip())
      boat.exec_action(*action)

  return boat.get_distance()

if __name__ == "__main__":
  print(main())

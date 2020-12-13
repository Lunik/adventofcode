from part1 import parseLine, Boat

class Boat2(Boat):
  def __init__(self, waypoint):
    super(Boat2, self).__init__('E')
    self.waypoint = waypoint

  def rotate(self, direction, angle):
    new_waypoint = dict(N=0, E=0, S=0, W=0)

    cardinals = list(self.waypoint.keys())

    if direction == 'R':
      for c in cardinals:
        new_waypoint[c] = self.waypoint[cardinals[int((cardinals.index(c) - (angle/90)) % len(cardinals))]]
    else:
      for c in cardinals:
        new_waypoint[c] = self.waypoint[cardinals[int((cardinals.index(c) + (angle/90)) % len(cardinals))]]

    self.waypoint = new_waypoint

  def execAction(self, action, value):
    if action in ['N', 'S', 'E', 'W']:
      self.waypoint[action] += value

    elif action in ['R', 'L']:
      self.rotate(action, value)

    elif action == "F":
      for direction in self.waypoint.keys():
        self.navigation[direction] += self.waypoint[direction] * value

  def debug(self):
    print(self.waypoint, self.navigation)

if __name__ == "__main__":
  boat = Boat2(dict(
    N=1,
    E=10,
    S=0,
    W=0))

  with open('input.txt', 'r') as f:
    for line in f:
      action = parseLine(line.strip())
      boat.execAction(*action)

  print(boat.getDistance())
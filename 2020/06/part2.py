from functools import reduce

def parseGroups(data):
  return map(
    lambda g: reduce(               # Map for each groups
      lambda a, b: set(a) & set(b), # Calculate intersection of all answers by groups
      filter(
        lambda r: r != '',          # Removing empty line wich can distort intersection caclulation
        g.split('\n'))),
    data.split('\n\n'))

def verify(groups):
  return reduce(
    lambda a, b: (a if type(a) is int else len(a)) + len(b), # Add all length of groups sets (after intersections)
    groups)

if __name__ == "__main__":
  with open('input.txt', 'r') as f:
    groups = parseGroups(f.read())

  print(verify(groups))
from functools import reduce

def parseGroups(data):
  return map(lambda g: set(g.replace('\n', '')), data.split('\n\n'))

def verify(groups):
  return reduce(lambda a, b: (len(a) if type(a) is set else a) + len(b), groups)

if __name__ == "__main__":
  with open('input.txt', 'r') as f:
    groups = parseGroups(f.read())

  print(verify(groups))
import re
from functools import reduce

def parseContains(bags):
  bags = bags.strip()
  if bags == 'no other bags.':
    return []

  return re.match('(\d+) ([\w ]+) bags?', bags).groups()

def parseRule(line):
  data = line.split('contain')

  bag = re.match('([\w ]+) bags', data[0].strip()).groups()[0]

  contain = list(map(parseContains, data[1].split(',')))

  return (bag, contain)

COUNTS = dict()

def containColor(color, rule, rules):
  if rule in COUNTS:
    return COUNTS[rule]

  if rule == color:
    COUNTS[rule] = [1]
    return COUNTS[rule]

  contains = rules[rule]

  counts = []

  for contain in contains:
    if len(contain) == 0:
      return

    if contain[1] not in COUNTS:
      recurse = containColor(color, contain[1], rules)
    else:
      recurse = COUNTS[contain[1]]

    if recurse is None:
      continue
    
    counts.append(recurse * int(contain[0]))

  COUNTS[rule] = counts if len(counts) > 0 else None
  return COUNTS[rule]

def sumTree(tree):
  if type(tree) == int:
    return tree

  if type(tree) == list and len(tree) == 0:
    return 0

  return sum(map(sumTree, tree))

if __name__ == "__main__":
  rules = dict()

  with open('input.txt', 'r') as f:
    for line in f:
      bag, contain = parseRule(line.strip())
      rules[bag] = contain

  color = 'shiny gold'

  result = 0
  for rule in rules.keys():
    tree = containColor(color, rule, rules)
    if tree is not None and sumTree(tree) > 0 and rule != color:
      result += 1

  print(result)
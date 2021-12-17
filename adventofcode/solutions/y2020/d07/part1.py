import re
import os


def parse_contains(bags):
  bags = bags.strip()
  if bags == 'no other bags.':
    return []

  return re.match('(\\d+) ([\\w ]+) bags?', bags).groups()


def parse_rule(line):
  data = line.split('contain')

  bag = re.match('([\\w ]+) bags', data[0].strip()).groups()[0]

  contain = list(map(parse_contains, data[1].split(',')))

  return (bag, contain)

COUNTS = {}


def contain_color(color, rule, rules):
  if rule in COUNTS:
    return COUNTS[rule]

  if rule == color:
    COUNTS[rule] = [1]
    return COUNTS[rule]

  contains = rules[rule]

  counts = []

  for contain in contains:
    if len(contain) == 0:
      return None

    if contain[1] not in COUNTS:
      recurse = contain_color(color, contain[1], rules)
    else:
      recurse = COUNTS[contain[1]]

    if recurse is None:
      continue

    counts.append(recurse * int(contain[0]))

  COUNTS[rule] = counts if len(counts) > 0 else None
  return COUNTS[rule]


def sum_tree(tree):
  if isinstance(tree, int):
    return tree

  if isinstance(tree, list) and len(tree) == 0:
    return 0

  return sum(map(sum_tree, tree))


def main():
  rules = {}

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    for line in file:
      bag, contain = parse_rule(line.strip())
      rules[bag] = contain

  color = 'shiny gold'

  result = 0
  for rule in rules:
    tree = contain_color(color, rule, rules)
    if tree is not None and sum_tree(tree) > 0 and rule != color:
      result += 1

  return result


if __name__ == "__main__":
  print(main())

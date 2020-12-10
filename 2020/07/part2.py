import re
from functools import reduce

from part1 import parseContains, parseRule

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

def countBag(color, rules):
  res = sum(map(
    lambda rule: int(rule[0]) * countBag(rule[1], rules) if \
      len(rule) > 0
      else 0,
    rules[color]))

  return res + 1

if __name__ == "__main__":
  rules = dict()

  with open('input.txt', 'r') as f:
    for line in f:
      bag, contain = parseRule(line.strip())
      rules[bag] = contain

  bag = 'shiny gold'

  print(countBag(bag, rules) - 1) # Remove the gold case from the count
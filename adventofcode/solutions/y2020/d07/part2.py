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

def count_bag(color, rules):
  res = sum(map(
    lambda rule: int(rule[0]) * count_bag(rule[1], rules) if \
      len(rule) > 0
      else 0,
    rules[color]))

  return res + 1

def main():
  rules = dict()

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    for line in file:
      bag, contain = parse_rule(line.strip())
      rules[bag] = contain

  bag = 'shiny gold'

  return count_bag(bag, rules) - 1 # Remove the gold case from the count

if __name__ == "__main__":
  print(main())
  
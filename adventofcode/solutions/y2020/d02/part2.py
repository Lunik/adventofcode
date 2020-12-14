import os

from adventofcode.solutions.y2020.d02.part1 import parse_line

def verify(policy, passwd):
  return policy[0][0] <= len(passwd) \
    and policy[0][1] <= len(passwd) \
    and ( \
      (passwd[policy[0][0]-1] == policy[1]) \
      ^ (passwd[policy[0][1]-1] == policy[1])) # XOR

def main():
  valid_tuples = 0

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    for line in file:
      res = parse_line(line)
      if verify(*res):
        valid_tuples += 1

  return valid_tuples

if __name__ == "__main__":
  print(main())

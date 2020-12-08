from part1 import parsePolicy, parseLine

def verify(policy, passwd):
  return policy[0][0] <= len(passwd) \
    and policy[0][1] <= len(passwd) \
    and ( \
      (passwd[policy[0][0]-1] == policy[1]) \
      ^ (passwd[policy[0][1]-1] == policy[1])) # XOR

if __name__ == "__main__":
  valid_tuples = 0

  with open('input.txt', 'r') as f:
    for line in f:
      res = parseLine(line)
      if verify(*res):
        valid_tuples += 1

  print(valid_tuples)
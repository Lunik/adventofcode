import sys

def parsePolicy(string):
  data = string.split(' ')

  count = list(map(lambda n: int(n), data[0].split('-')))

  letter = data[1].strip()

  return (count, letter)

def parseLine(line):
  data = line.strip().split(':')

  policy = parsePolicy(data[0])
  passwd = data[1].strip()

  return (policy, passwd)

def verify(policy, passwd):
  count = passwd.count(policy[1])
  return count >= policy[0][0] and count <= policy[0][1]

if __name__ == "__main__":
  valid_tuples = 0

  with open('input.txt', 'r') as f:
    for line in f:
      res = parseLine(line)
      if verify(*res):
        valid_tuples += 1

  print(valid_tuples)
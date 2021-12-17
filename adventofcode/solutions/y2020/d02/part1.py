import os


def parse_policy(string):
  data = string.split(' ')

  count = list(map(int, data[0].split('-')))

  letter = data[1].strip()

  return (count, letter)


def parse_line(line):
  data = line.strip().split(':')

  policy = parse_policy(data[0])
  passwd = data[1].strip()

  return (policy, passwd)


def verify(policy, passwd):
  count = passwd.count(policy[1])
  return count in range(policy[0][0], policy[0][1] + 1)


def main():
  valid_tuples = 0

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    for line in file:
      res = parse_line(line)
      if verify(*res):
        valid_tuples += 1

  return valid_tuples


if __name__ == "__main__":
  print(main())

import os
import cProfile
import pstats
import re
import math

def parse(file):
  monkeys = []

  buffer = ""
  for line in file:
    line = line.strip('\n')
    if line == "":

      res = re.match(r'Monkey (\d+):\n\s+Starting items: (.*)\n\s+Operation: new = (.*)\n\s+Test: divisible by (\d+)\n\s+If true: throw to monkey (\d+)\n\s+If false: throw to monkey (\d+)', buffer)
      #res = re.match(r'Monkey (\d+):\n\s+Starting items: ((\d+),?)*.*', buffer)

      monkey = list(res.groups())
      monkey[1] = list(map(int, monkey[1].split(', ')))
      for i in [0, 3, 4, 5]:
        monkey[i] = int(monkey[i])
      monkey.append(0)

      #code = compile(f"f = lambda old: {monkey[2]}", "<string>", "exec")
      #exec(code, globals(), locals())
      #monkey[2] = locals()['f']

      monkeys.append(monkey)

      buffer = ""
    else:
      buffer += line + "\n"

  return monkeys

def solve(monkeys, rounds=20, reduce_worry=True):
  # This prevent to have too large numbers
  # We find the least common multiple and modulo to this value
  lcm = math.lcm(*[monkey[3] for monkey in monkeys])

  for i in range(rounds):
    for monkey in monkeys:
      for item_id, item in enumerate(monkey[1]):
        monkey[6] += 1

        monkey[1][item_id] = eval(monkey[2], dict(old=item))
        if reduce_worry:
          monkey[1][item_id] //= 3
        else:
          monkey[1][item_id] %= lcm

        if monkey[1][item_id] % monkey[3]:
          # Not divisible
          monkeys[monkey[5]][1].append(monkey[1][item_id])
        else:
          # Divisible
          monkeys[monkey[4]][1].append(monkey[1][item_id])

      monkey[1] = []

  res = [0, 0]
  for monkey in monkeys:
    res.append(monkey[6])
    res = sorted(res, reverse=True)[:2]

  return res[0] * res[1]

def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    data = parse(file)

  return solve(data, rounds=20)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

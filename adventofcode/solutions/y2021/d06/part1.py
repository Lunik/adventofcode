import os
import cProfile
import pstats

def generate_pool():
  fishes = {}
  for i in range(9):
    fishes[i] = 0

  return fishes


def parse_data(data, pool):
  for fish in data.split(','):
    pool[int(fish)] += 1


def count_fish(pool):
  return sum(pool.values())


def exec_day(pool):
  mothers = pool[0]

  for i in range(1, 9):
    pool[i-1] = pool[i]

  pool[8] = mothers
  pool[6] += mothers


def run_loop(days, pool):
  for _ in range(days):
    exec_day(pool)

def main():
  pool = generate_pool()

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    line = file.read()

  parse_data(line, pool)

  run_loop(80, pool)

  return count_fish(pool)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

import os
import cProfile
import pstats


def verify(num1, num2):
  if num1 + num2 == 2020:
    return num1 * num2

  return None


def main():
  counter = 0

  last_number = None
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    for line in file:
      current_number = int(line)
      if last_number is not None:
        counter += 1 if current_number > last_number else 0
      last_number = current_number

  return counter


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

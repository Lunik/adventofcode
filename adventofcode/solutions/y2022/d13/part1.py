import os
import cProfile
import pstats

def parse(file):
  pairs = []

  pair = []
  for line in file:
    line = line.strip('\n')

    if len(line) == 0:
      pairs.append(pair)
      pair = []
      continue

    pair.append(eval(line))

  return pairs

def compare(list1, list2):
  for i in range(max([len(list1), len(list2)])):
    try:
      if type(list1[i]) == type(list2[i]) == int:
        if list1[i] > list2[i]:
          return 1
        elif list1[i] < list2[i]:
          return -1

      elif type(list1[i]) == type(list2[i]) == list:
        res = compare(list1[i], list2[i])
        if res in [-1, 1]:
          return res

      else:
        if type(list1[i]) == int:
          res = compare([list1[i]], list2[i])
          if res in [-1, 1]:
            return res
        elif type(list2[i]) == int:
          res = compare(list1[i], [list2[i]])
          if res in [-1, 1]:
            return res
    except IndexError as e:
      if len(list1) > len(list2):
        return 1
      elif len(list1) < len(list2):
        return -1

  return 0

def solve(pairs):

  result = 0
  
  for index, pair in enumerate(pairs):
    res = compare(*pair)
    if res == -1:
      result += index+1

  return result

def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    data = parse(file)

  return solve(data)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

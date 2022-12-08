import os
import cProfile
import pstats

def parse(file):
  matrix = []
  for line in file:
    matrix.append(list(line.strip('\n')))

  return matrix

def solve(matrix):
  total = 0

  for i in range(1, len(matrix)-1):
    for j in range(1, len(matrix[i])-1):
      if matrix[i][j] <= max(matrix[i][:j]) \
        and matrix[i][j] <= max(matrix[i][j+1:]) \
        and matrix[i][j] <= max([c[j] for c in matrix[:i]]) \
        and matrix[i][j] <= max([c[j] for c in matrix[i+1:]]):
        total += 1

  return (len(matrix)*len(matrix[i])) - total

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

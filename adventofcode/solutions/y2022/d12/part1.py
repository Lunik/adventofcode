import os
import cProfile
import pstats
from queue import PriorityQueue
import math
from collections import defaultdict
from copy import deepcopy

def parse(file):
  matrix = []

  start = None
  end = None

  for index, line in enumerate(file):
    line = list(line.strip('\n'))

    if 'S' in line:
      y = line.index('S')
      line[y] = 'a'
      start = (index, y)

    if 'E' in line:
      y = line.index('E')
      line[y] = 'z'
      end = (index, y)

    matrix.append(line)

  return matrix, start, end

def get_neighbors(pos, maxs):
  neighbors = list(filter(
    lambda p: (p[0] >= 0 and p[0] < maxs[0]) and (p[1] >= 0 and p[1] < maxs[1]),
    [(pos[0] - 1, pos[1]), (pos[0], pos[1] - 1), (pos[0] + 1, pos[1]), (pos[0], pos[1] + 1)]
  ))

  return neighbors

def dist(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def find_path(matrix, start, end):
  size = (len(matrix), len(matrix[0]))

  # Dictionary containing case count to get there
  # In key, the case coordinates
  # In value, the minimal distange found to get there
  distances = defaultdict(lambda: math.inf, {(0, 0): 0})

  # Priority queue to first handle smaller distance value
  q = PriorityQueue()
  q.put((0, (0, start)))

  while q.qsize() > 0:
    _, case = q.get()

    # Reached the end
    if case[1] == end:
      return distances

    # Loop on all the neighbors
    for neighbor in get_neighbors(case[1], size):
      case_letter = matrix[case[1][0]][case[1][1]]
      neighbor_letter = matrix[neighbor[0]][neighbor[1]]

      diff = ord(neighbor_letter) - ord(case_letter)
      if diff <= 1:

        # Calculate new distance
        new_path_distange = case[0] + 1

        # If we have found a new path to a case that have a smaller distance value
        if new_path_distange < distances[neighbor]:
          # Store the new distance value to get to this case
          distances[neighbor] = new_path_distange
          # Put the neighboor in the handle queue
          q.put((new_path_distange, (new_path_distange, neighbor)))


def print_matrix(matrix):
  for line in matrix:
    print(''.join(line))

def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    matrix, start, end = parse(file)

  res = find_path(matrix, start, end)

  return res[end]


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

import os
import cProfile
import pstats

from adventofcode.solutions.y2021.d04.part1 import parse, check_number, verify, calculate_solution

def main():

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    winning_numbers, grids = parse([line.strip() for line in file])

  winning_grid = None
  winning_number = None
  for winning_number in winning_numbers:
    for grid_index, grid in enumerate(grids):
      check_number(grid, winning_number)
      result = verify(grid)
      if result is not None:
        if len(grids) == 1:
          winning_grid = grids[0]
          break

        grids[grid_index] = None

    if winning_grid is not None:
      break

    grids = list(filter(None, grids))

  return calculate_solution(winning_number, result, winning_grid)


if __name__ == "__main__":
  with cProfile.Profile() as pr:
    print(main())

  stats = pstats.Stats(pr)
  stats.sort_stats(pstats.SortKey.TIME)
  stats.print_stats()

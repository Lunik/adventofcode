import os


from adventofcode.solutions.y2020.d15.part1 import parse_data, play


def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    number_list = parse_data(file.read())

  return play(number_list, 30000000)


if __name__ == "__main__":
  print(main())

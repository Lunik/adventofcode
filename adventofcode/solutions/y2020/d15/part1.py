import os


def parse_data(data):
  return [int(x) for x in data.split(',')]


def play(number_list, until):
  brain = dict()
  turn = 0
  last = None
  while turn < until:
    if turn < len(number_list):
      brain[number_list[turn]] = turn + 1
      last = number_list[turn]
    else:
      # If the last number is not in the brain
      if last not in brain:
        # This is the first time we saw him
        say_number = 0
      # else (the number is already in the brain)
      else:
        # Calculate since how many turn we have not seen the number
        say_number = turn - brain[last]

      # Update the last time we have seen the last number
      brain[last] = turn

      # The number we say became the new last
      last = say_number

    turn += 1


  return last


def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    number_list = parse_data(file.read())

  return play(number_list, 2020)


if __name__ == "__main__":
  print(main())

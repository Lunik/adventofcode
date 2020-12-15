import os
import re


def parse_mask(line):
  groups = re.match('^ = ([0-1X]+)$', line)

  return groups.groups()[0]


def parse_affectation(line):
  groups = re.match('^mem\\[([0-9]+)\\] = ([0-9]+)$', line)

  return [int(x) for x in groups.groups()]


def parse_data(data):
  blocks = data.split('mask')

  sequences = []

  for block in blocks[1:]:
    lines = block.split('\n')
    mask = parse_mask(lines[0])

    affectations = []

    for aff_line in lines[1:]:
      if aff_line.strip() != '':
        affectations.append(parse_affectation(aff_line))

    sequences.append((mask, affectations))

  return sequences


def int_to_bin(number):
  return "{0:036b}".format(number)


def bin_to_int(binary_string):
  return int(binary_string, 2)


def calculate_value(mask, value):
  binary_string = int_to_bin(value)

  new_binary_string = ''

  for index, bit in enumerate(binary_string):
    if mask[index] == 'X':
      new_binary_string += bit
    else:
      new_binary_string += mask[index]

  return bin_to_int(new_binary_string)


def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    instructions = parse_data(file.read())

  memory = dict()

  for instruction in instructions:
    for affectation in instruction[1]:
      memory[affectation[0]] = calculate_value(instruction[0], affectation[1])

  return sum(memory.values())


if __name__ == "__main__":
  print(main())

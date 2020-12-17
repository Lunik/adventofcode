import os

from adventofcode.solutions.y2020.d16.part1 import parse_data, passport_error_rate


def advanced_filter(possible_attribute_positions, rules, passport):
  for attribute, ranges in rules.items():
    for index, value in enumerate(passport):
      # Test if a give attribute could match all passport values at this index
      if value not in ranges and index in possible_attribute_positions[attribute]:
        # This attribute cannot be at this index otherwise this passport will we invalid
        possible_attribute_positions[attribute].remove(index)


def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    rules, my_passport, passports = parse_data(file.read())

  valid_passports = list(filter(lambda p: passport_error_rate(rules, p) == 0, passports))

  del rules['all']

  # At the begining, all attributes can be at all positions
  possible_attribute_positions = dict()

  for attr in rules:
    possible_attribute_positions[attr] = list(range(len(my_passport)))


  for passport in valid_passports:
    advanced_filter(possible_attribute_positions, rules, passport)

  departure_attributes = list(filter(
    lambda a: 'departure' in a,
    possible_attribute_positions.keys()))

  positions = dict()

  while len(positions.keys()) < len(rules.keys()):
    for attribute in set(possible_attribute_positions.keys()) ^ set(positions.keys()):
      attr_positions = set(possible_attribute_positions[attribute]) ^ set(positions.values())

      if len(attr_positions) == 1:
        positions[attribute] = attr_positions.pop()


    # The challenge answer only require attributes containing "derparture"
    # We can stop if we found the position of all of then
    found_departure_attributes = list(filter(lambda a: 'departure' in a, positions.keys()))
    if len(found_departure_attributes) == len(departure_attributes):
      break

  result_count = 1

  for attr in departure_attributes:
    result_count *= my_passport[positions[attr]]

  return result_count


if __name__ == "__main__":
  print(main())

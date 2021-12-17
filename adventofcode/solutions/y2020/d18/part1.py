import os
import re


class Calculator:
  def __init__(self, operations):
    self.operations = operations

  def calculate(self):
    buff = None
    operation = None
    for char in self.operations:
      if isinstance(char, Calculator):
        char = char.calculate()

      if char in ["+", "*"]:
        operation = char
      else:
        if buff is None:
          buff = char

        elif operation is not None:
          buff = eval("".join([str(buff), operation, str(char)]))
          operation = None

    return buff

  def __str__(self):
    return "(" + " ".join([str(o) for o in self.operations]) + ")"


def parse_line(deep, line):
  parenthesis_level = 0

  operations = []
  jump_index = 0

  for index, char in enumerate(line):
    if char == " ":
      continue

    if index < jump_index:
      continue

    if char == "(":
      parenthesis_level += 1
      return_index, calculator = parse_line(deep+1, line[index + 1:])
      jump_index = index + return_index + 3
      operations.append(calculator)

    elif char == ")":
      parenthesis_level -= 1
      if deep > 0:
        return (index-1, Calculator(operations))

    else:
      operations.append(char)

  return Calculator(operations)



def main():
  total = 0

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    for line in file:
      calculator = parse_line(0, line.strip())

      total += calculator.calculate()

  return total


if __name__ == "__main__":
  print(main())

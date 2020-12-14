import os


def verify(num1, num2):
  if num1 + num2 == 2020:
    return num1 * num2

  return None


def main():
  numbers = []

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    for line in file:
      numbers.append(int(line.strip()))

    for num1 in numbers:
      for num2 in numbers:
        res = verify(num1, num2)
        if res is not None:
          return res

  return None


if __name__ == "__main__":
  print(main())

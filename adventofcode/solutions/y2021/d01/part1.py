import os


def verify(num1, num2):
  if num1 + num2 == 2020:
    return num1 * num2

  return None


def main():
  counter = 0

  last_number = None
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    for line in file:
      current_number = int(line)
      if last_number is not None:
        counter += 1 if current_number > last_number else 0
      last_number = current_number

  return counter


if __name__ == "__main__":
  print(main())

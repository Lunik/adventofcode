import os


def verify(num1, num2):
  if num1 + num2 == 2020:
    return num1 * num2

  return None


def main(window_size=3):
  counter = 0

  window_1 = []
  window_2 = []
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    for line in file:
      current_number = int(line)
      if len(window_1) >= window_size:
        window_2 = window_1
        window_1 = window_1[1:]

      window_1.append(current_number)

      if len(window_2) >= window_size:
        counter += 1 if sum(window_1) > sum(window_2) else 0

  return counter


if __name__ == "__main__":
  print(main())

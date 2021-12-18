import os

def main():
  data = []

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    data = list(file.readline()[:-1])
    for index, line in enumerate(file):
      data = [int(l1) + int(l2) for l1, l2 in zip(data, list(line))]

  length = index + 2

  gamma_rate = []
  epsilon_rate = []
  for i in list(data):
    gamma_rate.append('1' if i/length > 0.5 else '0')
    epsilon_rate.append('0' if i/length > 0.5 else '1')

  result = int(''.join(gamma_rate), 2) * int(''.join(epsilon_rate), 2)

  return result


if __name__ == "__main__":
  print(main())

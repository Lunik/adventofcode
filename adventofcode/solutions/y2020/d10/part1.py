import os


def main():
  adapters = []
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    for line in file:
      adapters.append(int(line))

  adapters.sort()

  adapters.append(adapters[len(adapters) - 1] + 3) # Ad the device max joltage

  current_joltage = 0

  jolts_diff = [0, 0, 0]

  for adapter in adapters:
    jolts_diff[(adapter - current_joltage) - 1] += 1

    current_joltage = adapter

  return jolts_diff[0] * jolts_diff[2]


if __name__ == "__main__":
  print(main())

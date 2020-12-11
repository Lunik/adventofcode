
if __name__ == "__main__":

  adapters = []
  with open('input.txt') as f:
    for line in f:
      adapters.append(int(line))

  adapters.sort()

  adapters.append(adapters[len(adapters) - 1] + 3) # Ad the device max joltage

  current_joltage = 0

  jolts_diff = [0, 0, 0]

  for adapter in adapters:
    jolts_diff[(adapter - current_joltage) - 1] += 1

    current_joltage = adapter

  print(jolts_diff[0] * jolts_diff[2])

import sys

numbers = []

with open('input.txt', 'r') as f:
  for line in f:
    numbers.append(int(line.strip()))

  res = list(map(
    lambda n: list(map(
      lambda m: print(n*m) if n+m == 2020 else '',
      numbers)),
    numbers))

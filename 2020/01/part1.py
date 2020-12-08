import sys

numbers = []

def verify(n, m):
  if n+m == 2020:
    print(n*m)
    sys.exit(0) 

with open('input.txt', 'r') as f:
  for line in f:
    numbers.append(int(line.strip()))

  res = list(map(
    lambda n: list(map(
      lambda m: verify(n, m),
      numbers)),
    numbers))

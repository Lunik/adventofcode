import sys

numbers = []

def verify(n, m, o):
  if n+m+o == 2020:
    print(n*m*o)
    sys.exit(0) 

with open('input.txt', 'r') as f:
  for line in f:
    numbers.append(int(line.strip()))

  res = list(map(
    lambda n: list(map(
      lambda m: list(map(
        lambda o: verify(n, m, o),
        numbers)),
      numbers)),
    numbers))
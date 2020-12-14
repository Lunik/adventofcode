import os


def verify(encryption_set, number):
  for num1 in encryption_set:
    for num2 in encryption_set:
      if num1 + num2 == number:
        return True

  return False


def find_invalid_numer(encryption_offset, sequence):
  encryption_set = []

  for number in sequence:
    if len(encryption_set) < encryption_offset:
      encryption_set.append(number)
      continue

    if not verify(encryption_set, number):
      return number

    encryption_set.append(number)

    encryption_set = encryption_set[1:len(encryption_set)]

  return None


def main():
  encryption_offset = 25

  sequence = []

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    for line in file:
      sequence.append(int(line))

  return find_invalid_numer(encryption_offset, sequence)


if __name__ == "__main__":
  print(main())

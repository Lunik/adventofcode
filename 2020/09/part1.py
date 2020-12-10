
def verify(encryption_set, number):
  for x in encryption_set:
    for y in encryption_set:
      if x + y == number:
        return True

  return False

def findInvalidNumber(encryption_offset, sequence):
  encryption_set = []

  for number in sequence:
    if len(encryption_set) < encryption_offset:
      encryption_set.append(number)
      continue

    if not verify(encryption_set, number):
      return number

    encryption_set.append(number)

    encryption_set = encryption_set[1:len(encryption_set)]

if __name__ == "__main__":

  encryption_offset = 25

  sequence = []

  with open('input.txt') as f:
    for line in f:
      sequence.append(int(line))

  print(findInvalidNumber(encryption_offset, sequence))
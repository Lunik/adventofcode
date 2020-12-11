
def isValid(value, sequence):
  return value in sequence

ALREADY_CHECKED_FROM = dict()

def testAllSubsequences(start, sequence):

  if start in ALREADY_CHECKED_FROM:    # If we have already tested all possible sequences from this start
    return ALREADY_CHECKED_FROM[start]

  if start == sequence[-1]: # If this is the final device
    return 1                # Then sequence is valid

  valid_sequences = 0

  for jump in range(1, 4):              # Test all possible jumps form 1 to 3
    if isValid(start + jump, sequence):
      valid_sequences += testAllSubsequences(start + jump, sequence) # Test subsequences with that jump


  ALREADY_CHECKED_FROM[start] = valid_sequences

  return valid_sequences

if __name__ == "__main__":

  adapters = []
  with open('input.txt') as f:
    for line in f:
      adapters.append(int(line))

  adapters.sort()

  adapters.append(adapters[len(adapters) - 1] + 3) # Ad the device max joltage

  print(testAllSubsequences(0, adapters))

import os

def parse_sequence(sequence):
  res_sequence = []

  for index, element in enumerate(sequence):
    if element == 'x':
      continue

    res_sequence.append((int(element), int(index)))

  return res_sequence

def parse_data(data):
  data = data.split('\n')

  return parse_sequence(data[1].split(','))

def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    sequence = parse_data(file.read())

  current_time = 0 # Begin at T = 1
  step = 1         # Increate time by step value

  # For all buses
  for bus_schedule, bus_offset in sequence:
    # Find time where this bus arrives at station
    # Bus must be decaled in time based on theire position \
    # in the list so we add offset to the current time
    while (current_time + bus_offset) % bus_schedule != 0:
      # while not at station increase time by the step value
      current_time += step

    step *= bus_schedule # Make the step value a factor of the bu schedule

  return current_time

# Notes :
#   - For the first interation of the loop, we search for a time where bus[0] is at station
#     - step is equal at 1 so we test all times until :
#       - When we found one and we keep the current time
#     - We turn the step into a factor of the bus schedule
#       - That way, during the next  interation of the loop \
#          we only test time value that can be divided by the previous bus
#         - So we are sure that the previous bus is at station for all time we test
#         - So if the current bus is at station we now that \
#            the two buses are at station at the same time
#   - We do that for all buses
#     - At the end we should find a time where all the buses are at station
if __name__ == "__main__":
  print(main())

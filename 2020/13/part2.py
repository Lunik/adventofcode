
def parseData(data):
  data = data.split('\n')

  return BusCalendar(data[1].split(','))

class BusCalendar:
  def __init__(self, sequence):
    self.sequence = []

    for index, el in enumerate(sequence):
      if el == 'x':
        continue

      self.sequence.append((int(el), int(index)))

if __name__ == "__main__":

  with open('input.txt', 'r') as f:
    bus_calendar = parseData(f.read())

  current_time = 0 # Begin at T = 1
  step = 1         # Increate time by step value
  
  for bus_schedule, bus_offset in bus_calendar.sequence:   # For all buses
    while (current_time + bus_offset) % bus_schedule != 0: # Find time where this bus arrives at station | Bus must be decaled in time based on theire position in the list so we add offset to the current time
      current_time += step                                 # while not at station increase time by the step value

    step *= bus_schedule # Make the step value a factor of the bu schedule

  print(current_time)

#
# Notes : 
#   - For the first interation of the loop, we search for a time where bus[0] is at station
#     - step is equal at 1 so we test all times until :
#       - When we found one and we keep the current time
#     - We turn the step into a factor of the bus schedule
#       - That way, during the next  interation of the loop we only test time value that can be divided by the previous bus
#         - So we are sure that the previous bus is at station for all time we test
#         - So if the current bus is at station we now that the two buses are at station at the same time
#   - We do that for all buses
#     - At the end we should find a time where all the buses are at station
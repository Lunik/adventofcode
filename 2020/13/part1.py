
def parseData(data):
  data = data.split('\n')

  bus_calendar = BusCalendar(int(data[0]))

  for schedule in data[1].split(','):
    if schedule == 'x':
      continue

    bus_calendar.registerBus(Bus(int(schedule)))

  return bus_calendar

class Bus:
  def __init__(self, schedule):
    self.schedule = schedule
    self.atStation = True

  def move(self, timestamp):
    self.atStation = True if (timestamp % self.schedule) == 0 else False

  def debug(self):
    print('  Bus :', self.schedule, '\t', ' not' if not self.atStation else '', 'at station')

class BusCalendar:
  def __init__(self, current_timestamp):
    self.current_timestamp = current_timestamp
    self.buses = []

  def registerBus(self, bus):
    bus.move(self.current_timestamp)
    self.buses.append(bus)

  def waitNextTimestamp(self):
    self.current_timestamp += 1

  def findBus(self):
    for bus in self.buses:
      bus.move(self.current_timestamp)
      if bus.atStation:
        return bus

    return None

  def debug(self):
    print('Timestamp', self.current_timestamp)
    for bus in self.buses:
      bus.debug()

if __name__ == "__main__":

  with open('input.txt', 'r') as f:
    bus_calendar = parseData(f.read())

  start_time = bus_calendar.current_timestamp

  bus_found = None
  while bus_found is None:
    bus_calendar.waitNextTimestamp()
    bus_found = bus_calendar.findBus()

    #bus_calendar.debug()

  print((bus_calendar.current_timestamp - start_time) * bus_found.schedule)
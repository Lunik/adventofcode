import os


def parse_data(data):
  data = data.split('\n')

  bus_calendar = BusCalendar(int(data[0]))

  for schedule in data[1].split(','):
    if schedule == 'x':
      continue

    bus_calendar.register_bus(Bus(int(schedule)))

  return bus_calendar


class Bus:
  def __init__(self, schedule):
    self.schedule = schedule
    self.atStation = True

  def move(self, timestamp):
    self.atStation = (timestamp % self.schedule) == 0

  def debug(self):
    print('  Bus :', self.schedule, '\t', ' not' if not self.atStation else '', 'at station')


class BusCalendar:
  def __init__(self, current_timestamp):
    self.currentTimestamp = current_timestamp
    self.buses = []

  def register_bus(self, bus):
    bus.move(self.currentTimestamp)
    self.buses.append(bus)

  def wait_next_timestamp(self):
    self.currentTimestamp += 1

  def find_bus(self):
    for bus in self.buses:
      bus.move(self.currentTimestamp)
      if bus.atStation:
        return bus

    return None

  def debug(self):
    print('Timestamp', self.currentTimestamp)
    for bus in self.buses:
      bus.debug()


def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    bus_calendar = parse_data(file.read())

  start_time = bus_calendar.currentTimestamp

  bus_found = None
  while bus_found is None:
    bus_calendar.wait_next_timestamp()
    bus_found = bus_calendar.find_bus()

    #bus_calendar.debug()

  return (bus_calendar.currentTimestamp - start_time) * bus_found.schedule


if __name__ == "__main__":
  print(main())

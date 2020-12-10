
def parseLine(line):
  data = line.split(' ')

  return (data[0], int(data[1].replace('+', '')))

def handleNop(pointer, accumulator, value):
  return (pointer + 1, accumulator)

def handleAcc(pointer, accumulator, value):
  return (pointer + 1, accumulator + value)

def handleJmp(pointer, accumulator, value):
  return (pointer + value, accumulator)

ACTIONS = dict(
    nop=handleNop,
    acc=handleAcc,
    jmp=handleJmp)

def runProgram(program):
  pointer = 0
  visited = []
  accumulator = 0
  aborted = False

  while pointer < len(program):
    if pointer in visited:
      aborted = True
      break
    visited.append(pointer)
    instruction = program[pointer]
    pointer, accumulator = ACTIONS[instruction[0]](pointer, accumulator, instruction[1])

  return (pointer, accumulator, aborted)


if __name__ == "__main__":

  program = []

  with open('input.txt') as f:
    for line in f:
      program.append(parseLine(line.strip()))

  pointer, accumulator, aborted = runProgram(program)

  print(accumulator)
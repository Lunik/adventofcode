from part1 import runProgram, parseLine

def findNextPossibleCorruptedInstruction(after, program):
  after += 1
  while program[after][0] not in ['nop', 'jmp']:
    after += 1

  return after

def fixProgram(corrupted_instruction, program):
  program[corrupted_instruction] = (
    'jmp' if program[corrupted_instruction][0] == 'nop' else 'nop',
    program[corrupted_instruction][1]
  )

  return program

if __name__ == "__main__":

  orig_program = []

  with open('input.txt') as f:
    for line in f:
      orig_program.append(parseLine(line.strip()))

  aborted = True
  corrupted_instruction = -1

  while aborted and corrupted_instruction < (len(orig_program) - 1):
    corrupted_instruction = findNextPossibleCorruptedInstruction(corrupted_instruction, orig_program)
    program = fixProgram(corrupted_instruction, orig_program[:]) # Force duplication of object orig_program
    pointer, accumulator, aborted = runProgram(program)

  print(accumulator)

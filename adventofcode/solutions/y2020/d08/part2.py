import os


from adventofcode.solutions.y2020.d08.part1 import run_program, parse_line


def find_next_possible_corrupted_instruction(after, program):
  after += 1
  while program[after][0] not in ['nop', 'jmp']:
    after += 1

  return after


def fix_program(corrupted_instruction, program):
  program[corrupted_instruction] = (
    'jmp' if program[corrupted_instruction][0] == 'nop' else 'nop',
    program[corrupted_instruction][1]
  )

  return program


def main():
  orig_program = []

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    for line in file:
      orig_program.append(parse_line(line.strip()))

  aborted = True
  corrupted_instruction = -1

  while aborted and corrupted_instruction < (len(orig_program) - 1):
    corrupted_instruction = find_next_possible_corrupted_instruction(
      corrupted_instruction,
      orig_program)
    # Force duplication of object orig_program
    program = fix_program(corrupted_instruction, orig_program[:])
    _, accumulator, aborted = run_program(program)

  return accumulator


if __name__ == "__main__":
  print(main())

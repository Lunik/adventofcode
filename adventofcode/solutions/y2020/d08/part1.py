import os


def parse_line(line):
    data = line.split(" ")

    return (data[0], int(data[1].replace("+", "")))


def handle_nop(pointer, accumulator, _):
    return (pointer + 1, accumulator)


def handle_acc(pointer, accumulator, value):
    return (pointer + 1, accumulator + value)


def handle_jmp(pointer, accumulator, value):
    return (pointer + value, accumulator)


ACTIONS = dict(nop=handle_nop, acc=handle_acc, jmp=handle_jmp)


def run_program(program):
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
        pointer, accumulator = ACTIONS[instruction[0]](
            pointer, accumulator, instruction[1]
        )

    return (pointer, accumulator, aborted)


def main():
    program = []

    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        for line in file:
            program.append(parse_line(line.strip()))

    _, accumulator, _ = run_program(program)

    return accumulator


if __name__ == "__main__":
    print(main())

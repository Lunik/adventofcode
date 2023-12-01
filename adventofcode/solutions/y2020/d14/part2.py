import os
import re


from adventofcode.solutions.y2020.d14.part1 import parse_data, int_to_bin, bin_to_int


def replace_x(binary_string):
    # If string is emptry return emptry possible values
    if binary_string == "":
        return [""]

    # If string don't contains 'X', there is no need to recurse further
    if "X" not in binary_string:
        return [binary_string]

    groups = re.match("^([0-1]+)?X?(.*)$", binary_string).groups()

    res = replace_x(groups[1])

    binary_strings = []
    prefix = groups[0] if groups[0] is not None else ""

    for binary_part in res:
        binary_strings.append(prefix + "0" + binary_part)
        binary_strings.append(prefix + "1" + binary_part)

    return binary_strings


def calculate_value(mask, value):
    binary_string = int_to_bin(value)

    new_binary_string = ""

    for index, _ in enumerate(binary_string):
        if mask[index] == "0":
            new_binary_string += binary_string[index]
        elif mask[index] == "1":
            new_binary_string += mask[index]
        else:
            new_binary_string += "X"

    memory_addresses = replace_x(new_binary_string)

    return map(bin_to_int, memory_addresses)


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        instructions = parse_data(file.read())

    memory = {}

    for instruction in instructions:
        for affectation in instruction[1]:
            addresses = calculate_value(instruction[0], affectation[0])
            for addresse in addresses:
                memory[addresse] = affectation[1]

    return sum(memory.values())


if __name__ == "__main__":
    print(main())

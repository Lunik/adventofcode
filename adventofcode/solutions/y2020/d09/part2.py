import os


from adventofcode.solutions.y2020.d09.part1 import find_invalid_numer


def find_sum_match(sum_count, sum_to_find, sequence):
    for start in range(0, len(sequence) - sum_count):
        subset_sequence = sequence[start:sum_count]
        if sum(subset_sequence) == sum_to_find:
            return subset_sequence

    return None


def main():
    encryption_offset = 25

    sequence = []

    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        for line in file:
            sequence.append(int(line))

    invalid_number = find_invalid_numer(encryption_offset, sequence)

    sum_count = 2

    while sum_count <= len(sequence):
        result = find_sum_match(sum_count, invalid_number, sequence)

        if result is not None:
            break

        sum_count += 1

    return max(result) + min(result)


if __name__ == "__main__":
    print(main())

import os


def is_valid(value, sequence):
    return value in sequence


ALREADY_CHECKED_FROM = {}


def test_all_subsequences(start, sequence):
    # If we have already tested all possible sequences from this start
    if start in ALREADY_CHECKED_FROM:
        return ALREADY_CHECKED_FROM[start]

    # If this is the final device
    if start == sequence[-1]:
        # Then sequence is valid
        return 1

    valid_sequences = 0

    # Test all possible jumps form 1 to 3
    for jump in range(1, 4):
        if is_valid(start + jump, sequence):
            # Test subsequences with that jump
            valid_sequences += test_all_subsequences(start + jump, sequence)

    ALREADY_CHECKED_FROM[start] = valid_sequences

    return valid_sequences


def main():
    adapters = []
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        for line in file:
            adapters.append(int(line))

    adapters.sort()

    # Ad the device max joltage
    adapters.append(adapters[len(adapters) - 1] + 3)

    return test_all_subsequences(0, adapters)


if __name__ == "__main__":
    print(main())

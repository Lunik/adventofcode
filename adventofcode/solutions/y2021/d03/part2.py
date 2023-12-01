import os
import cProfile
import pstats


def calculate(the_list, index, keep_max=False):
    counter = 0

    new_lists = [[], []]

    for element in the_list:
        if element[index] == "1":
            counter += 1
            new_lists[0].append(element)
        else:
            counter -= 1
            new_lists[1].append(element)

    if counter < 0:
        if keep_max:
            result = new_lists[1]
        else:
            result = new_lists[0]
    elif counter > 0:
        if keep_max:
            result = new_lists[0]
        else:
            result = new_lists[1]
    else:
        if keep_max:
            result = new_lists[0]
        else:
            result = new_lists[1]

    return result


def main():
    numbers = []

    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        for line in file:
            numbers.append(list(line)[:-1])

    new_list = calculate(numbers, 0, keep_max=True)

    for index in range(1, len(numbers[0])):
        new_list = calculate(new_list, index, keep_max=True)

        if len(new_list) == 1:
            break

    oxygen_generator_rating = int("".join(new_list[0]), 2)

    new_list = calculate(numbers, 0, keep_max=False)

    for index in range(1, len(numbers[0])):
        new_list = calculate(new_list, index, keep_max=False)

        if len(new_list) == 1:
            break

    co2_scrubber_rating = int("".join(new_list[0]), 2)

    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

import os


def parse_ranges(raw_ranges):
    raw_ranges = raw_ranges.split("or")

    ranges = set([])

    for a_range in raw_ranges:
        a_range = a_range.split("-")

        ranges = ranges.union(set(range(int(a_range[0]), int(a_range[1]) + 1)))

    return ranges


def parse_rules(data):
    data = data.split("\n")

    rules = dict(all=set([]))

    for line in data:
        line = line.split(":")
        field = line[0]
        ranges = parse_ranges(line[1].strip())

        rules[field] = ranges
        rules["all"] = rules["all"].union(ranges)

    return rules


def parse_passport(line):
    return [int(x) for x in line.split(",")]


def parse_mypassport(data):
    data = data.split("\n")

    return parse_passport(data[1])


def parse_passports(data):
    data = data.split("\n")

    passports = []

    for line in data[1:]:
        if line != "":
            passports.append(parse_passport(line))

    return passports


def parse_data(data):
    data = data.split("\n\n")

    rules = parse_rules(data[0])
    my_passport = parse_mypassport(data[1])
    passports = parse_passports(data[2])

    return (rules, my_passport, passports)


def passport_error_rate(rules, passport):
    error_rate = 0

    for value in passport:
        if value not in rules["all"]:
            error_rate += value

    return error_rate


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        rules, _, passports = parse_data(file.read())

    return sum(map(lambda p: passport_error_rate(rules, p), passports))


if __name__ == "__main__":
    print(main())

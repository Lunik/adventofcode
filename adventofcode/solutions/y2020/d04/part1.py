import os


def parse_attr(attr):
    return attr.split(":")


def parse_passport(line):
    attrs = line.replace("\n", " ").split(" ")

    return dict(map(parse_attr, attrs))


def parse_file(data):
    lines = data.strip().split("\n\n")

    return map(parse_passport, lines)


def is_valid(required_attr, ignore_attr, passport):
    require_diff = set(required_attr) ^ set(passport.keys())
    ignore_diff = set(ignore_attr) ^ set(require_diff)

    return len(require_diff) == 0 or len(ignore_diff) == 0


def verify(required_attr, ignore_attr, passports):
    valid_passports = []
    for passport in passports:
        if is_valid(required_attr, ignore_attr, passport):
            valid_passports.append(passport)

    return valid_passports


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        passports = parse_file(file.read())

    valid_passports = verify(
        ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"], ["cid"], passports
    )

    return len(valid_passports)


if __name__ == "__main__":
    print(main())

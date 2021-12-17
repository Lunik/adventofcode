import re
import os

from functools import reduce


from adventofcode.solutions.y2020.d04.part1 import parse_file, is_valid

def check_range(val_range, value):
  value = int(value)
  return value in range(val_range[0], val_range[1] + 1)

def regex_groups(regex, value):
  res = re.match(regex, value)
  return [] if res is None else res.groups()

def check_byr(value):
  return len(str(value)) == 4 and check_range([1920, 2002], value)

def check_iyr(value):
  return len(str(value)) == 4 and check_range([2010, 2020], value)

def check_eyr(value):
  return len(str(value)) == 4 and check_range([2020, 2030], value)

def check_hgt(value):
  match_groups = regex_groups('(\\d+)(cm|in)', value)
  return len(match_groups) == 2 \
    and (check_range([150, 193], match_groups[0]) \
      if match_groups[1] == 'cm' \
      else check_range([59, 76], match_groups[0]))

def check_pid(value):
  return len(regex_groups('(\\d{9})', value)) == 1 \
    and (len(str(value)) == 9)

def check_hcl(value):
  return len(regex_groups('(#[0-9a-f]{6})', value)) == 1

def check_ecl(value):
  return len(regex_groups('(amb|blu|brn|gry|grn|hzl|oth)', value)) == 1

checkDict = dict(
  byr=check_byr,
  iyr=check_iyr,
  eyr=check_eyr,
  hgt=check_hgt,
  pid=check_pid,
  hcl=check_hcl,
  ecl=check_ecl,
  cid=lambda v: True)

def is_valid_extended(passport):
  return reduce(lambda a, b: a and b, map(lambda key: checkDict[key](passport[key]), passport))

def verify(required_attr, ignore_attr, passports):
  valid_passports = []
  for passport in passports:
    if is_valid(required_attr, ignore_attr, passport) and is_valid_extended(passport):
      valid_passports.append(passport)

  return valid_passports

def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    passports = parse_file(file.read())

  valid_passports = verify(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'], ['cid'], passports)

  return len(valid_passports)

if __name__ == "__main__":
  print(main())

import re
from functools import reduce

from part1 import parseFile, isValid

def checkRange(val_range, value):
  value = int(value)
  return value >= val_range[0] and value <= val_range[1]

def regexGroups(regex, value):
  res = re.match(regex, value)
  return [] if res is None else res.groups()

def checkByr(value):
  return len(str(value)) == 4 and checkRange([1920, 2002], value)

def checkIyr(value):
  return len(str(value)) == 4 and checkRange([2010, 2020], value)

def checkEyr(value):
  return len(str(value)) == 4 and checkRange([2020, 2030], value)

def checkHgt(value):
  match_groups = regexGroups('(\d+)(cm|in)', value)
  return len(match_groups) == 2 \
    and (checkRange([150, 193], match_groups[0]) \
      if match_groups[1] == 'cm' \
      else checkRange([59, 76], match_groups[0]))

def checkPid(value):
  return len(regexGroups('(\d{9})', value)) == 1 \
    and (len(str(value)) == 9)

def checkHcl(value):
  return len(regexGroups('(#[0-9a-f]{6})', value)) == 1

def checkEcl(value):
  return len(regexGroups('(amb|blu|brn|gry|grn|hzl|oth)', value)) == 1

checkDict = dict(
  byr=checkByr,
  iyr=checkIyr,
  eyr=checkEyr,
  hgt=checkHgt,
  pid=checkPid,
  hcl=checkHcl,
  ecl=checkEcl,
  cid=lambda v: True)

def isValidExtended(passport):
  return reduce(lambda a, b: a and b, map(lambda key: checkDict[key](passport[key]), passport))

def verify(required_attr, ignore_attr, passports):
  valid_passports = []
  for passport in passports:
    if isValid(required_attr, ignore_attr, passport) and isValidExtended(passport):
      valid_passports.append(passport)

  return valid_passports

if __name__ == "__main__":
  with open('input.txt', 'r') as f:
    passports = parseFile(f.read())

  valid_passports = verify(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'], ['cid'], passports)

  print(len(valid_passports))
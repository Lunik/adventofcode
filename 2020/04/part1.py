
def parseAttr(attr):
  return attr.split(':')

def parsePassport(line):
  attrs = line.replace('\n', ' ').split(' ')

  return dict(list(map(parseAttr, attrs)))

def parseFile(data):
  lines = data.strip().split('\n\n')

  return list(map(parsePassport, lines))

def isValid(required_attr, ignore_attr, passport):
  require_diff = set(required_attr) ^ set(passport.keys())
  ignore_diff = set(ignore_attr) ^ set(require_diff)

  return len(require_diff) == 0 or len(ignore_diff) == 0

def verify(required_attr, ignore_attr, passports):
  valid_passports = []
  for passport in passports:
    if isValid(required_attr, ignore_attr, passport):
      valid_passports.append(passport)

  return valid_passports

if __name__ == "__main__":
  with open('input.txt', 'r') as f:
    passports = parseFile(f.read())

  valid_passports = verify(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'], ['cid'], passports)

  print(len(valid_passports))
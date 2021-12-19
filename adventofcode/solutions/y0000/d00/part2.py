import os

def main():
  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r', encoding='UTF-8') as file:
    for line in file:
      print(line)

  return "TODO"


if __name__ == "__main__":
  print(main())

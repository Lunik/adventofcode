import os

def main():
  oxygen_generator_rating = 0
  CO2_scrubber_rating = 0

  with open(os.path.join(os.path.dirname(__file__), 'input.txt'), 'r') as file:
    for line in file:
      pass

  return oxygen_generator_rating * CO2_scrubber_rating


if __name__ == "__main__":
  print(main())

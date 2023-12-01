import os


from adventofcode.solutions.y2020.d12.part1 import parse_line, Boat


class Boat2(Boat):
    def __init__(self, waypoint):
        super().__init__("E")
        self.waypoint = waypoint

    def rotate(self, direction, angle):
        new_waypoint = dict(N=0, E=0, S=0, W=0)

        cardinals = list(self.waypoint.keys())

        if direction == "R":
            for cardinal in cardinals:
                new_waypoint[cardinal] = self.waypoint[
                    cardinals[
                        int((cardinals.index(cardinal) - (angle / 90)) % len(cardinals))
                    ]
                ]
        else:
            for cardinal in cardinals:
                new_waypoint[cardinal] = self.waypoint[
                    cardinals[
                        int((cardinals.index(cardinal) + (angle / 90)) % len(cardinals))
                    ]
                ]

        self.waypoint = new_waypoint

    def exec_action(self, action, value):
        if action in ["N", "S", "E", "W"]:
            self.waypoint[action] += value

        elif action in ["R", "L"]:
            self.rotate(action, value)

        elif action == "F":
            for direction in self.waypoint.keys():
                self.navigation[direction] += self.waypoint[direction] * value

    def debug(self):
        print(self.waypoint, self.navigation)


def main():
    boat = Boat2(dict(N=1, E=10, S=0, W=0))

    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        for line in file:
            action = parse_line(line.strip())
            boat.exec_action(*action)

    return boat.get_distance()


if __name__ == "__main__":
    print(main())

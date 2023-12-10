import os
import cProfile
import pstats
import re


def parse_seed(line):
    line = line.strip("\n")
    m = re.findall(r"\d+", line)
    m = map(int, m)
    return list([range(x, x) for x in m])


def parse_map(data):
    lines = data.split("\n")
    name = lines[0].split(" ")[0]

    result_map = []

    for line in lines[1:-1]:
        destination, source, offset = line.split(" ")
        destination = int(destination)
        source = int(source)
        offset = int(offset)

        result_map.append(
            {
                "source_range": range(source, source + offset),
                "source": source,
                "destination": destination,
            }
        )

    return name, result_map


def parse(file, parse_seed_func=parse_seed, parse_map_func=parse_map):
    maps = dict()

    seeds = parse_seed_func(file.readline())
    file.readline()

    current_map = ""
    for line in file:
        if line == "\n":
            name, data = parse_map_func(current_map)
            maps[name] = data
            current_map = ""
        else:
            current_map += line

    name, data = parse_map_func(current_map)
    maps[name] = data

    return seeds, maps


# range1 :    ======
# range2 :  ==============
def range_fully_in_range(range1, range2):
    return range1.start >= range2.start and range1.stop <= range2.stop


# range1 :  =======
# range2 :     ============
def range_partially_right_in_range(range1, range2):
    return (
        range1.start < range2.start
        and range1.stop <= range2.stop
        and range1.stop >= range2.start
    )


# range1 :     =======
# range2 :  ========
def range_partially_left_in_range(range1, range2):
    return (
        range1.start >= range2.start
        and range1.stop > range2.stop
        and range1.start <= range2.stop
    )


# range1 :  ==============
# range2 :     =======
def range_fully_in_range_reverse(range1, range2):
    return range1.start < range2.start and range1.stop > range2.stop


def solve(seeds, maps):
    for map_name, map_data in maps.items():
        updated_seeds = []
        for data_range in map_data:
            leftover_seeds = []
            for seed_range in seeds:
                if range_fully_in_range(seed_range, data_range["source_range"]):
                    updated_seeds.append(
                        range(
                            (seed_range.start - data_range["source"])
                            + data_range["destination"],
                            (seed_range.stop - data_range["source"])
                            + data_range["destination"],
                        )
                    )

                elif range_fully_in_range_reverse(
                    seed_range, data_range["source_range"]
                ):
                    leftover_seeds.append(
                        range(seed_range.start, data_range["source_range"].start - 1)
                    )
                    updated_seeds.append(
                        range(
                            (data_range["source_range"].start - data_range["source"])
                            + data_range["destination"],
                            (data_range["source_range"].stop - data_range["source"])
                            + data_range["destination"],
                        )
                    )
                    leftover_seeds.append(
                        range(data_range["source_range"].stop + 1, seed_range.stop)
                    )

                elif range_partially_right_in_range(
                    seed_range, data_range["source_range"]
                ):
                    leftover_seeds.append(
                        range(seed_range.start, data_range["source_range"].start - 1)
                    )
                    updated_seeds.append(
                        range(
                            (data_range["source_range"].start - data_range["source"])
                            + data_range["destination"],
                            (seed_range.stop - data_range["source"])
                            + data_range["destination"],
                        )
                    )

                elif range_partially_left_in_range(
                    seed_range, data_range["source_range"]
                ):
                    updated_seeds.append(
                        range(
                            (seed_range.start - data_range["source"])
                            + data_range["destination"],
                            (data_range["source_range"].stop - data_range["source"])
                            + data_range["destination"],
                        )
                    )
                    leftover_seeds.append(
                        range(data_range["source_range"].stop + 1, seed_range.stop)
                    )

                else:
                    leftover_seeds.append(seed_range)
            seeds = leftover_seeds

        seeds = updated_seeds + leftover_seeds

    return min([x.start for x in seeds])


def main():
    with open(
        os.path.join(os.path.dirname(__file__), "input.txt"), "r", encoding="UTF-8"
    ) as file:
        data = parse(file)

    return solve(*data)


if __name__ == "__main__":
    with cProfile.Profile() as pr:
        print(main())

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats()

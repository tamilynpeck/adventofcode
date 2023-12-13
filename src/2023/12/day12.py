from itertools import combinations_with_replacement


class Day12:
    def __init__(self, data):
        self.data = data

    def solve_part_one(self):
        total_arrangements = [self.possible_arrangements(line) for line in self.data]
        return sum(total_arrangements)

    def solve_part_two(self):
        pass

    def possible_arrangements(self, line):
        springs, records = line.split(" ")
        records = [int(i) for i in records.split(",")]
        # springs = [c for c in springs.split(".") if c]
        print(springs, records)
        arrangements = 0

        # if len(springs) == len(records):
        #     matches = [len(spring) == records[i] for i, spring in enumerate(springs)]
        #     if all(matches):
        #         return 1
        operational = "."
        operational_index = [i for i, c in enumerate(springs) if c == operational]
        # print(operational_index)
        # options, 1, 2, 3, operational, broken, unknown
        operational = 1
        broken = 2
        # where the records line up with the springs

        test = 0
        print(len(springs))
        combinations = combinations_with_replacement([1, 2], len(springs))

        for comb in list(combinations):
            if test > 10:
                break
            if not all(comb[i] == operational for i in operational_index):
                # print("not all", comb)
                # test += 1
                continue
            test += 1

            print(comb)
            # break

        return arrangements

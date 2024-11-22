OPERATIONAL = "."
DAMAGED = "#"
UNKNOWN = "?"


class Day12:
    def __init__(self, data):
        self.data = data

    def solve_part_one(self):
        total_arrangements = [self.possible_arrangements(line) for line in self.data]
        return sum(total_arrangements)

    def solve_part_two(self):
        pass

    def possible_arrangements(self, line):
        springs, damaged_groups = line.split(" ")
        damaged_groups = [int(i) for i in damaged_groups.split(",")]
        damaged_parts = ["".join([DAMAGED * i]) for i in damaged_groups]
        max_gaps = len(damaged_parts) + 1

        print(springs, damaged_groups)
        print(damaged_parts)
        print(max_gaps)

        arrangements = 0
        operational_index = [i for i, c in enumerate(springs) if c == OPERATIONAL]
        # solve for unknowns
        # has to be at least one operational between each damaged part
        print(len(springs))

        if Day12.is_match(springs.replace(UNKNOWN, DAMAGED), damaged_groups):
            arrangements += 1

        return arrangements

    @staticmethod
    def is_match(pattern, damaged_groups):
        print("is_match", pattern, damaged_groups)
        counts = []
        group_len = 0
        for l in pattern:
            if l == DAMAGED:
                group_len += 1
            if l != DAMAGED and group_len > 0:
                counts.append(group_len)
                group_len = 0

        return counts == damaged_groups

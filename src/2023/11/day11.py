class Day11:
    def __init__(self, data):
        self.data = data
        self.expanded_universe = self.expand_universe()
        self.transposed_expanded_universe = [
            "".join(r) for r in zip(*self.expanded_universe)
        ]

        self.map = {}

    def solve_part_one(self):
        i = 1
        for r, row in enumerate(self.expanded_universe):
            for c, col in enumerate(row):
                if col != "#":
                    continue
                self.map[i] = {"loc": (r, c)}
                i += 1

        total_distance = []
        for k, v in self.map.items():
            for key, value in self.map.items():
                if k >= key:
                    continue
                dist = self.distance(v["loc"], value["loc"])
                total_distance.append(dist)

        return sum(total_distance)

    def solve_part_two(self, exp_distance=2):
        i = 1
        for r, row in enumerate(self.expanded_universe):
            for c, col in enumerate(row):
                if col != "#":
                    continue
                self.map[i] = {"loc": (r, c)}
                i += 1

        total_distance = []
        for k, v in self.map.items():
            for key, value in self.map.items():
                if k >= key:
                    continue
                dist = self.distance(v["loc"], value["loc"], exp_distance)
                total_distance.append(dist)

        return sum(total_distance)

    def distance(self, a, b, exp_value_amount=2):
        a_r, a_c = a
        b_r, b_c = b
        dist = abs(a_r - b_r) + abs(a_c - b_c)

        expand_indicator = "*"
        a_expand_lookup = self.expanded_universe[a_r][
            min([a_c, b_c]) : max([a_c, b_c]) + 1
        ]
        b_expand_lookup = self.transposed_expanded_universe[b_c][a_r : b_r + 1]
        a_counts = a_expand_lookup.count(expand_indicator)
        b_counts = b_expand_lookup.count(expand_indicator)

        adj_exp_value = exp_value_amount - 1
        return dist + (a_counts * adj_exp_value) + (b_counts * adj_exp_value)

    def expand_universe(self):
        exp_line_value = "*"
        expanded = []
        for line in self.data:
            if all([c != "#" for c in line]):
                expanded.append([exp_line_value] * len(line))
            else:
                expanded.append(line)

        t_matrix = zip(*expanded)
        expanded_cols = []
        for row in t_matrix:
            if all([c != "#" for c in row]):
                expanded_cols.append([exp_line_value] * len(row))
            else:
                expanded_cols.append(row)

        expanded = zip(*expanded_cols)
        expanded = ["".join(row) for row in expanded]

        return expanded

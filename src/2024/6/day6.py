class Day6:
    def __init__(self, data):
        self.original_data = [list(row) for row in data]
        self.data = [list(row) for row in self.original_data]

        # method to set guard location to a new value
        self._get_value = lambda loc: self.data[loc[0]][loc[1]]
        # move guard lambda, return guard location plus direction
        self._move_guard_to = lambda guard_loc, dir: (
            guard_loc[0] + dir[0],
            guard_loc[1] + dir[1],
        )

    def _set_value(self, loc, value):
        self.data[loc[0]][loc[1]] = value

    def print_data(self):
        for row in self.data:
            print("".join(row))

    def solve_part_one(self):
        self.solve_guard_path()

        self.print_data()
        return sum([row.count("X") for row in self.data])

    def solve_part_two(self):
        loop_locations = []

        for r, row in enumerate(self.data):
            for c, _ in enumerate(row):
                self.data = [list(row) for row in self.original_data]
                value = self._get_value((r, c))
                if value == "#" or value == "^":
                    continue
                self._set_value((r, c), "O")
                if self.solve_guard_path():
                    loop_locations.append((r, c))
                # print(f"Testing {r}, {c}")
                # self.print_data()

                self._set_value((r, c), value)

        return len(loop_locations)

    def get_guard_loc(self):
        guard = "^"
        guard_loc = None
        for i, row in enumerate(self.data):
            if guard in row:
                for j, col in enumerate(row):
                    if col == guard:
                        guard_loc = (i, j)
                        break
        return guard_loc

    def out_of_bounds(self, loc):
        return (
            loc[0] < 0
            or loc[1] < 0
            or loc[0] >= len(self.data)
            or loc[1] >= len(self.data[0])
        )

    def solve_guard_path(self):
        guard_up = "^"
        guard_right = ">"
        guard_down = "v"
        guard_left = "<"

        guard_dir_map = {
            guard_up: (-1, 0),
            guard_right: (0, 1),
            guard_down: (1, 0),
            guard_left: (0, -1),
        }

        guard_rotation_map = {
            guard_up: guard_right,
            guard_right: guard_down,
            guard_down: guard_left,
            guard_left: guard_up,
        }

        guard_loc = self.get_guard_loc()
        loop_count = 0
        max_loop = sum([len(row) for row in self.data])
        while True:
            if max_loop == loop_count:
                return True
            loop_count += 1
            try:
                if not guard_loc:
                    # print("No guard_loc", loop_count)
                    break
                guard_dir_value = self._get_value(guard_loc)
                current_dir = guard_dir_map[guard_dir_value]
                next_loc = self._move_guard_to(guard_loc, current_dir)
                if self.out_of_bounds(next_loc):
                    self._set_value(guard_loc, "X")
                    # print("Out of bounds", next_loc, loop_count)
                    break

                next_loc_value = self._get_value(next_loc)
                if next_loc_value == "#" or next_loc_value == "O":
                    self._set_value(guard_loc, guard_rotation_map[guard_dir_value])
                else:
                    self._set_value(guard_loc, "X")
                    self._set_value(next_loc, guard_dir_value)
                    guard_loc = next_loc

            except IndexError:
                # print("Index Error", guard_loc, next_loc_value)
                break

        return False

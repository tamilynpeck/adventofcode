offsets = {
    "U": (-1, 0),  # up
    "D": (1, 0),  # down
    "L": (0, -1),  # left
    "R": (0, 1),  # right
}


class Day18:
    def __init__(self, data):
        self.data = data
        self.map = [["#"]]

    def solve_part_one(self):
        r, c = 0, 0
        for line in self.data:
            direction, steps, _ = line.split(" ")
            print(direction, steps)
            for _ in range(int(steps)):
                if direction == "R":
                    c += 1
                elif direction == "L":
                    c -= 1
                elif direction == "U":
                    r -= 1
                elif direction == "D":
                    r += 1
                # print(step, r, c)
                if r >= len(self.map):
                    self.map.append(["." for _ in range(len(self.map[0]))])
                if c >= len(self.map[r]):
                    diff = c - len(self.map[r]) + 1
                    self.map[r].extend(["." for _ in range(diff)])
                if r == -1:
                    self.shift_map_up()
                    r = 0
                if c == -1:
                    self.shift_map_left()
                    c = 0

                self.map[r][c] = "#"

        self.print_data_map()

        for line in self.map:
            # print(line)
            indexes = [i for i, x in enumerate(line) if x == "#"]
            start_index = line.index("#")
            end_index = len(line) - 1 - line[::-1].index("#")
            fill_range = range(start_index, end_index + 1)
            # print(start_index, end_index)
            for i, _ in enumerate(line):
                if i in fill_range:
                    line[i] = "#"

        print("After filling:")
        self.print_data_map()

        return sum([row.count("#") for row in self.map])

    def shift_map_left(self):
        for row in self.map:
            row.insert(0, ".")

    def shift_map_up(self):
        self.map.insert(0, ["." for _ in range(len(self.map[0]))])

    def print_data_map(self):
        for row in self.map:
            # print(row)
            print(" ".join(row))

    def solve_part_two(self):
        pass

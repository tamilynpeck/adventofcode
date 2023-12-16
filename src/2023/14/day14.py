class Day14:
    def __init__(self, data):
        self.data = data
        self.data = [list(line) for line in self.data]
        self.print_data()

    def print_data(self):
        for line in self.data:
            print("".join(line))

    def solve_part_one(self):
        self.roll_north()
        return self.get_total_load()

    def solve_part_two(self, cycles=1):
        for i in range(cycles):
            # print("cycle", i)
            self.roll_north()
            self.roll_west()
            self.roll_south()
            self.roll_east()

        return self.get_total_load()

    def get_total_load(self):
        total_load = []
        number_of_rows = len(self.data)
        for r, line in enumerate(self.data):
            for c, cell in enumerate(line):
                if cell == "O":
                    total_load.append(number_of_rows - r)

        return sum(total_load)

    def roll(self):
        for r, line in enumerate(self.data):
            # print(r, line)
            for c, cell in enumerate(line):
                if cell != "O" or r == 0:
                    continue

                for i in range(r + 1):
                    current_row = r - i
                    above_row = r - (i + 1)
                    # print(i, current_row, above_row, "".join(self.data[above_row]))
                    if current_row == 0 or self.data[above_row][c] == "#":
                        break
                    if self.data[above_row][c] == "O":
                        continue
                    self.data[above_row][c] = "O"
                    self.data[current_row][c] = "."

    def roll_north(self):
        self.roll()
        # print("----------roll_north")
        # self.print_data()

    def roll_west(self):
        # self.data = map(list, zip(*self.data))
        self.data = [list(line) for line in zip(*self.data)]
        self.roll()
        self.data = [list(line) for line in zip(*self.data)]

        # print("----------roll_west")
        # self.print_data()

    def roll_south(self):
        self.data.reverse()
        self.roll()
        self.data.reverse()

        # print("----------roll_south")
        # self.print_data()

    def roll_east(self):
        self.data = [list(line) for line in zip(*self.data)]
        self.data.reverse()
        self.roll()
        self.data.reverse()
        self.data = [list(line) for line in zip(*self.data)]

        # print("----------roll_east")
        # self.print_data()

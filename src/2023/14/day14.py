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
        total_load = 0
        number_of_rows = len(self.data)
        for r, line in enumerate(self.data):
            for cell in line:
                if cell == "O":
                    total_load += number_of_rows - r
        return total_load

    def roll(self):
        for r in range(1, len(self.data)):
            for c in range(len(self.data[r])):
                if self.data[r][c] == "O":
                    for i in range(r, 0, -1):
                        if self.data[i-1][c] == "#":
                            break
                        if self.data[i-1][c] == ".":
                            self.data[i-1][c] = "O"
                            self.data[i][c] = "."

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

class Day18:
    def __init__(self, data):
        # [x, y] or [col, row]
        self.data = [[int(i) for i in x.split(",")] for x in data]
        print(self.data)

    def print_grid(self):
        for row in self.grid:
            print("".join(row))

    def solve_part_one(self, size=70, bytes=1024):
        self.grid = [["." for x in range(0, size + 1)] for y in range(0, size + 1)]

        for i, (col, row) in enumerate(self.data):
            if i >= bytes:
                break
            self.grid[row][col] = "#"

        self.print_grid()

    def solve_part_two(self):
        pass

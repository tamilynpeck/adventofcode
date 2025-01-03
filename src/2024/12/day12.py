class Day12:
    def __init__(self, data):
        self.data = data
        print(self.data)

    def solve_part_one(self):

        pass

    def solve_part_two(self):
        for r, row in enumerate(self.data):
            for c, col in enumerate(row):
                print(col)

    def count_adjacent(self, r, c):
        pass

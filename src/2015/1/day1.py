class Day1:
    def __init__(self, data):
        self.data = data[0]
        self.transform = [1 if char in ("(") else -1 for char in self.data]

    def solve_part_one(self):
        return sum(self.transform)

    def solve_part_two(self):
        floor = 0
        for i, char in enumerate(self.transform):
            floor += char

            if floor == -1:
                return i + 1

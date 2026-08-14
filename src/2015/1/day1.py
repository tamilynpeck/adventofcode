class Day1:
    def __init__(self, data):
        self.data = data[0]
        print(f"data: {self.data}")
        self.data = [char for char in self.data if char in ("(", ")")]
        print(f"data: {self.data}")

    def solve_part_one(self):
        floor = 0
        for char in self.data:
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1

        return floor

    def solve_part_two(self):
        floor = 0
        for i, char in enumerate(self.data):
            print(f"char: {char}, floor: {floor}")
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1

            if floor == -1:
                return i + 1

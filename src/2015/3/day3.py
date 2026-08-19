class Day3:
    def __init__(self, data):
        self.data = [char for char in data[0] if char in [">", "<", "^", "v"]]

    def solve_part_one(self):
        locations = set()
        x, y = 0, 0
        locations.add((x, y))
        for move in self.data:
            if move == ">":
                x += 1
            elif move == "<":
                x -= 1
            elif move == "^":
                y += 1
            elif move == "v":
                y -= 1
            locations.add((x, y))

        return len(locations)

    def solve_part_two(self):
        locations = set()
        odd_x, odd_y = 0, 0
        even_x, even_y = 0, 0
        locations.add((odd_x, odd_y))
        for i, move in enumerate(self.data):
            if i % 2 == 0:
                if move == ">":
                    odd_x += 1
                elif move == "<":
                    odd_x -= 1
                elif move == "^":
                    odd_y += 1
                elif move == "v":
                    odd_y -= 1
                locations.add((odd_x, odd_y))

            if i % 2 == 1:
                if move == ">":
                    even_x += 1
                elif move == "<":
                    even_x -= 1
                elif move == "^":
                    even_y += 1
                elif move == "v":
                    even_y -= 1
                locations.add((even_x, even_y))

        return len(locations)

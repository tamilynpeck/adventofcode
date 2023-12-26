offsets = {
    "U": (-1, 0),  # up
    "D": (1, 0),  # down
    "L": (0, -1),  # left
    "R": (0, 1),  # right
}

hex_directions = {
    "3": "U",  # up
    "1": "D",  # down
    "2": "L",  # left
    "0": "R",  # right
}


class Day18:
    def __init__(self, data):
        self.data = data

    def solve_part_one(self):
        instructions = []
        for line in self.data:
            direction, steps, _ = line.split(" ")
            steps = int(steps)
            instructions.append((direction, steps))

        return self.solve_for_points(instructions)

    def solve_for_points(self, instructions):
        r, c = 0, 0
        self.map = [(r, c)]
        self.map = []
        boundary_points = 0
        # print(": (", r, ",", c, ")")
        for direction, steps in instructions:
            boundary_points += steps
            r, c = r + offsets[direction][0] * steps, c + offsets[direction][1] * steps
            # print(direction, steps, ": (", r, ",", c, ")")
            self.map.append((r, c))

        shoelace_area = shoelace(self.map)

        # pick's theorem
        return int(shoelace_area + 1 + boundary_points / 2)

    def solve_part_two(self):
        instructions = []
        for line in self.data:
            _, hex = line.split("#")
            steps = int(hex[:5], 16)
            direction = hex_directions[hex[5]]
            steps = int(steps)
            instructions.append((direction, steps))

        return self.solve_for_points(instructions)


# shoelace formula
def shoelace(points):
    area = 0

    X = [point[0] for point in points] + [points[0][0]]
    Y = [point[1] for point in points] + [points[0][1]]

    for i in range(len(points)):
        area += X[i] * Y[i + 1] - Y[i] * X[i + 1]

    return abs(area) / 2

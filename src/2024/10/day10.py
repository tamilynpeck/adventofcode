DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
]


class Day10:
    def __init__(self, data):
        self.data = [[int(x) if x.isdigit() else x for x in list(row)] for row in data]
        self.print_data()

    def print_data(self):
        for row in self.data:
            print("".join([str(x) for x in row]))

    def solve_part_one(self):
        trail_count = []

        for r, row in enumerate(self.data):
            for c, value in enumerate(row):
                if value == 0:
                    print(f"Found 0 at {r}, {c}")
                    trail_end_points = self.find_next_number(r, c, 1)
                    if trail_end_points:
                        print("Trail Score", trail_end_points)
                        trail_count.append(len(set(trail_end_points)))
        print(trail_count)
        return sum(trail_count)

    def solve_part_two(self):
        trail_count = []

        for r, row in enumerate(self.data):
            for c, value in enumerate(row):
                if value == 0:
                    print(f"Found 0 at {r}, {c}")
                    trail_end_points = self.find_next_number(r, c, 1)
                    if trail_end_points:
                        print("Trail Score", trail_end_points)
                        trail_count.append(len(trail_end_points))
        print(trail_count)
        return sum(trail_count)

    def find_next_number(self, r, c, number):
        trail_end_points = []

        print(f"Looking for {number} at {r}, {c}")

        for direction in DIRECTIONS:
            try:
                next_r, next_c = r + direction[0], c + direction[1]
                if next_r < 0 or next_c < 0:
                    raise IndexError
                if next_r >= len(self.data) or next_c >= len(self.data[0]):
                    raise IndexError

                next_value = self.data[next_r][next_c]
                if number == 9 and next_value == 9:
                    trail_end_points.append((next_r, next_c))
                    print(f"Found 9 at {next_r}, {next_c}")
                elif next_value == number:
                    points = self.find_next_number(next_r, next_c, number + 1)
                    if points:
                        trail_end_points.extend(points)
            except IndexError:
                continue

        return trail_end_points

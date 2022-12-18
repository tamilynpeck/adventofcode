from collections import Counter


class HydrothermalVenture:
    def __init__(self, input, diagonal=False):
        self.diagonal = diagonal
        self.input = self.format_input(input)
        self.all_points = []
        self.map_lines()
        self.overlap_points = self.sum_overlapping_points()

    def format_input(self, input):
        matrix = []
        for row in input:
            values = row.split(" -> ")
            values = [v.split(",") for v in values]
            values = [[int(value) for value in r] for r in values]
            if (
                self.diagonal
                or values[0][0] == values[1][0]
                or values[0][1] == values[1][1]
            ):
                matrix.append(values)

        return matrix

    def build_range(value1, value2):
        increment = 1 if value1 < value2 else -1
        return range(value1, value2 + increment, increment)

    @staticmethod
    def build_diagonal_line(row):
        line = []
        x1, y1 = row[0]
        x2, y2 = row[1]
        x = [*HydrothermalVenture.build_range(x1, x2)]
        y = [*HydrothermalVenture.build_range(y1, y2)]
        for i in range(0, len(x)):
            line.extend([f"{x[i]},{y[i]}"])
        return line

    def map_lines(self):
        for row in self.input:
            x1, y1 = row[0]
            x2, y2 = row[1]
            if x1 != x2 and y1 != y2:
                self.all_points.extend(HydrothermalVenture.build_diagonal_line(row))
            elif x1 != x2:
                points = [f"{x},{y1}" for x in HydrothermalVenture.build_range(x1, x2)]
                self.all_points.extend(points)
            elif y1 != y2:
                points = [f"{x1},{y}" for y in HydrothermalVenture.build_range(y1, y2)]
                self.all_points.extend(points)

    def sum_overlapping_points(self):
        count = 0
        counter = Counter(self.all_points)
        for _, value in counter.items():
            if value > 1:
                count += 1
        return count

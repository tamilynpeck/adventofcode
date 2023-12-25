# from scipy.stats import linregress
# import numpy as np
# from scipy.stats import linregress


class Day24:
    def __init__(self, data, min=200000000000000, max=400000000000000):
        self.data = [self.parse_hailstone(r) for r in data]
        self.min = min
        self.max = max

    def solve_part_one(self):
        # print(self.data)
        intersecting = []
        for a, line1 in enumerate(self.data):
            # print(a, line1)
            for b, line2 in enumerate(self.data):
                if a == b or b < a:
                    continue
                # print(a, b, line2)

                intersect = line_intersection(line1, line2)
                # print(intersect)
                if (
                    intersect
                    and self.within_test_area(intersect)
                    and not_in_past(line1, intersect)
                    and not_in_past(line2, intersect)
                ):
                    intersecting.append(intersect)

        # print(intersecting)
        return len(intersecting)

    def solve_part_two(self):
        pass

    def parse_hailstone(self, row):
        position, velocity = row.split("@")
        position = [int(x.strip()) for x in position.split(",")]
        velocity = [int(x.strip()) for x in velocity.split(",")]
        # x = [position[0], position[0] + velocity[0]]
        # y = [position[1], position[1] + velocity[1]]
        return position, velocity

    def within_test_area(self, intersect):
        x, y = intersect
        if x < self.min or x > self.max or y < self.min or y > self.max:
            return False
        return not any([x < self.min, x > self.max, y < self.min, y > self.max])


def not_in_past(line1, intersect):
    xI, yI = intersect
    x, y = line1[0][0], line1[0][1]
    xV, yV = line1[1][0], line1[1][1]
    if (xV > 0 and x > xI) or (yV > 0 and y > yI):
        return False
    if (xV < 0 and x < xI) or (yV < 0 and y < yI):
        return False
    return True


def line_list(position, velocity):
    x1, x2 = position[0], position[0] + velocity[0]
    y1, y2 = position[1], position[1] + velocity[1]
    return [(x1, y1), (x2, y2)]


def line_intersection(line1, line2):
    line1 = line_list(*line1)
    line2 = line_list(*line2)
    # print(line1, line2)
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return (x, y)

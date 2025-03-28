import heapq


class Day16:
    def __init__(self, data):
        self.data = [list(row) for row in data]
        self.print_data()

    def print_data(self):
        for row in self.data:
            print("".join(row))

    def solve_part_one(self):
        points = []
        for r, row in enumerate(self.data):
            for c, col in enumerate(row):
                if col == "S":
                    self.start = (r, c)
                if col == "E":
                    self.end = (r, c)
                if col == ".":
                    points.append((r, c))

        # rows, cols = len(self.data), len(self.data[0])
        start, end = self.start, self.end
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        distances = {point: float("inf") for point in points}
        distances[start] = 0

        heap = [(0, start)]
        while heap:
            print(heap)
            current_distance, current_point = heapq.heappop(heap)
            if current_point == end:
                return current_distance

            for dr, dc in directions:
                new_r, new_c = current_point[0] + dr, current_point[1] + dc
                new_point = (new_r, new_c)
                if new_point in distances:
                    new_distance = current_distance + 1
                    if new_distance < distances[new_point]:
                        distances[new_point] = new_distance
                        heapq.heappush(heap, (new_distance, new_point))

    def solve_part_two(self):
        pass

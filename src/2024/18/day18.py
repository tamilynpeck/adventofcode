import heapq


class Day18:
    def __init__(self, data):
        self.data = [[int(i) for i in x.split(",")] for x in data]

    def solve_part_one(self, size=70, bytes=1024):
        self.grid = [["." for x in range(0, size + 1)] for y in range(0, size + 1)]
        for i, (col, row) in enumerate(self.data):
            if i >= bytes:
                break
            self.grid[row][col] = "#"

        points = []
        for r, row in enumerate(self.grid):
            for c, col in enumerate(row):
                if col != "#":
                    points.append((r, c))

        start = (0, 0)
        end = (size, size)

        return self.dijkstra(start, end, points, size)

    def solve_part_two(self, size=70, bytes=1024):
        points = [(x, y) for x in range(0, size + 1) for y in range(0, size + 1)]
        start = (0, 0)
        end = (size, size)

        for i, (col, row) in enumerate(self.data):
            points.remove((row, col))
            if i >= bytes:
                continue

            reachable = self.dijkstra(start, end, points, size)
            if not reachable:
                return (col, row)

    def dijkstra(self, start, end, points, size):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        distances = {point: float("inf") for point in points}
        distances[start] = 0

        heap = [(0, start)]
        while heap:
            current_distance, current_point = heapq.heappop(heap)
            if current_point == end:
                return current_distance

            for dr, dc in directions:
                new_r, new_c = current_point[0] + dr, current_point[1] + dc
                new_point = (new_r, new_c)
                if 0 <= new_r <= size and 0 <= new_c <= size and new_point in points:
                    new_distance = current_distance + 1
                    if new_distance < distances[new_point]:
                        distances[new_point] = new_distance
                        heapq.heappush(heap, (new_distance, new_point))

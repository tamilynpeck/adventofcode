import pprint
import math

pp = pprint.PrettyPrinter(depth=4)


class Day10:
    def __init__(self, data):
        self.data = data
        self.map = [list(r) for r in data]
        self.start = None
        for x, row in enumerate(self.map):
            for y, col in enumerate(row):
                if col == "S":
                    self.start = (x, y)
                    break

        self.print_data_map()

        # print(self.data)
        # print(self.map)
        # print(self.start)

    def print_data_map(self):
        for row in self.map:
            print(" ".join(row))

    def solve_part_one(self):
        self.connections = {}

        x, y = self.start
        conn = (x, y)

        looking = True
        step = 0
        while looking:
            x, y = conn
            # print("conns", conn, self.map[x][y], step)

            if conn in self.connections.keys():
                print("found conn", conn)
                looking = False
                break

            next_conn = self.get_valid_connections(*conn)
            if not next_conn:
                self.connections[conn] = next_conn
                print("found no next_conn")
                looking = False
                break
            self.connections[conn] = next_conn
            step += 1

            if next_conn == self.start:
                # self.connections[conn] = self.start
                print("found start", conn)
                looking = False
                break
            conn = next_conn

        # print(self.connections)
        # pp.pprint(self.connections)
        return math.ceil(step / 2)

    def solve_part_two(self):
        self.solve_part_one()
        for x, row in enumerate(self.map):
            for y, _ in enumerate(row):
                if (x, y) not in self.connections.keys():
                    self.map[x][y] = "."

        count_in_loop = 0
        for x, row in enumerate(self.map):
            for y, col in enumerate(row):
                if self.map[x][y] != ".":
                    continue
                in_loop = self.location_in_loop(x, y)
                # if in_loop:
                #     self.map[x][y] = "I"
                #     count_in_loop += 1
                # else:
                #     self.map[x][y] = "O"

        print("          ")
        self.print_data_map()
        return count_in_loop

    def get_valid_connections(self, x, y):
        conns = []
        valid_offsets = curr_valid_connections[self.map[x][y]]
        for dir_x, dir_y in valid_offsets:
            next_x, next_y = x + dir_x, y + dir_y
            if next_x < 0 or next_y < 0:
                continue
            if next_x >= len(self.map) or next_y >= len(self.map[0]):
                continue
            value = self.map[next_x][next_y]
            if (
                value in next_valid_connections[(dir_x, dir_y)]
                and (next_x, next_y) not in self.connections.keys()
            ):
                conns.append((next_x, next_y))
        return conns[0] if conns else None

    def location_in_loop(self, x, y):
        pass


pipes = [
    "|",
    "-",
    "L",
    "J",
    "F",
    "7",
    "S",
]
offsets = [
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
]
curr_valid_connections = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    "7": [(1, 0), (0, -1)],
    "S": offsets,
}
next_valid_connections = {
    (-1, 0): ["|", "F", "7"],
    (1, 0): ["|", "L", "J"],
    (0, -1): ["-", "F", "L"],
    (0, 1): ["-", "J", "7"],
}

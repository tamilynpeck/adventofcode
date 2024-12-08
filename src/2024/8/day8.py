class Day8:
    def __init__(self, data):
        self.data = [list(row) for row in data]
        for row in self.data:
            print("".join(row))
        self.validated_anti_nodes = set()

    def solve_part_one(self):
        nodes = set([value for row in self.data for value in row if not value == "."])

        # map location of each value for each node type
        node_map = {}
        for node in nodes:
            node_map[node] = []
            for i, row in enumerate(self.data):
                for j, value in enumerate(row):
                    if value == node:
                        node_map[node].append((i, j))
        print(node_map)

        # get all possible paths between nodes of the same type
        paths = {}
        for node in nodes:
            paths[node] = []
            for i, loc in enumerate(node_map[node]):
                for j in range(i + 1, len(node_map[node])):
                    paths[node].append((loc, node_map[node][j]))
        print(paths)

        # continue the paths to create anti_nodes
        for _, value in paths.items():
            for start, end in value:

                distance = (end[0] - start[0], end[1] - start[1])
                reverse_distance = (distance[0] * -1, distance[1] * -1)
                print(start, end, " : ", distance, reverse_distance)

                self.create_anti_node(start, distance, (start, end))
                self.create_anti_node(start, reverse_distance, (start, end))
                self.create_anti_node(end, distance, (start, end))
                self.create_anti_node(end, reverse_distance, (start, end))

        return len(self.validated_anti_nodes)

    def solve_part_two(self):
        self.validated_anti_nodes = set()
        nodes = set([value for row in self.data for value in row if not value == "."])

        # map location of each value for each node type
        node_map = {}
        for node in nodes:
            node_map[node] = []
            for i, row in enumerate(self.data):
                for j, value in enumerate(row):
                    if value == node:
                        node_map[node].append((i, j))
        print(node_map)

        # get all possible paths between nodes of the same type
        paths = {}
        for node in nodes:
            paths[node] = []
            for i, loc in enumerate(node_map[node]):
                for j in range(i + 1, len(node_map[node])):
                    paths[node].append((loc, node_map[node][j]))
        print(paths)

        # continue the paths to create anti_nodes
        for _, value in paths.items():
            for start, end in value:
                distance = (end[0] - start[0], end[1] - start[1])
                reverse_distance = (distance[0] * -1, distance[1] * -1)

                self.create_continuing_anti_nodes(start, distance)
                self.create_continuing_anti_nodes(start, reverse_distance)
                self.create_continuing_anti_nodes(end, distance)
                self.create_continuing_anti_nodes(end, reverse_distance)

        return len(self.validated_anti_nodes)

    def create_anti_node(self, node, distance, values):
        try:
            x, y = node[0] + distance[0], node[1] + distance[1]

            if (x, y) in values:
                return
            if x < 0 or y < 0:
                return
            if x >= len(self.data) or y >= len(self.data[0]):
                return

            if self.data[x][y] != "#":
                self.data[x][y] = "#"
            self.validated_anti_nodes.add((x, y))
        except IndexError:
            pass

    def create_continuing_anti_nodes(self, node, distance):
        x, y = node[0], node[1]
        try:
            while True:
                x, y = x + distance[0], y + distance[1]

                if x < 0 or y < 0:
                    raise IndexError
                if x >= len(self.data) or y >= len(self.data[0]):
                    raise IndexError

                self.validated_anti_nodes.add((x, y))
                if self.data[x][y] == ".":
                    self.data[x][y] = "#"
        except IndexError:
            pass

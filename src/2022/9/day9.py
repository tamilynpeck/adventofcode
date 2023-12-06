class RopeBridge:
    def __init__(self, data: list):
        self.data = data
        self.motions = [RopeMove.parse(move) for move in self.data]
        self.motions = self.motions[0:20]
        self.board = Board()

    def simulate_motions(self):
        for move in self.motions:
            self.board.simulate_move(move)

        return self.board.count_visits()


class RopeMove:
    def __init__(self, direction, distance):
        self.direction = direction
        self.distance = distance

    @staticmethod
    def parse(move):
        direction, distance = move.split(" ")
        return RopeMove(direction, int(distance))

    def __repr__(self):
        return f"RopeMove({self.direction}, {self.distance})"


# H moves, then check if T moves
# x, y
# track the moves, and count the moves
move_map = {
    "R": lambda x, y: [x + 1, y],
    "L": lambda x, y: [x - 1, y],
    "U": lambda x, y: [x, y + 1],
    "D": lambda x, y: [x, y - 1],
}


class Board:
    def __init__(self):
        self.moves = []
        self.board = []
        self.head_position = [0, 0]
        self.tail_position = [0, 0]
        self.track_tail_positions = []

        self.move = lambda direction, x, y: move_map[direction](x, y)

    def simulate_move(self, move):
        self.moves.append(move)
        print(move)

        for _ in range(0, move.distance):
            self.head_position = self.move(move.direction, *self.head_position)
            self.move_tail_if_needed()
            print(self.head_position, self.tail_position)
            # print(">", self.track_tail_positions)

    def move_tail_if_needed(self):
        if self.tail_position == self.head_position:
            return

        x_tail, y_tail = self.tail_position
        x_head, y_head = self.head_position
        r_x_diff = x_head - x_tail
        l_x_diff = x_tail - x_head
        u_y_diff = y_head - y_tail
        d_y_diff = y_tail - y_head

        if u_y_diff > 1:
            self.tail_position = self.move("U", *self.tail_position)
        if d_y_diff > 1:
            self.tail_position = self.move("D", *self.tail_position)
        if l_x_diff > 1:
            self.tail_position = self.move("L", *self.tail_position)
        if r_x_diff > 1:
            self.tail_position = self.move("R", *self.tail_position)

        if self.tail_position not in self.track_tail_positions:
            self.track_tail_positions.append(self.tail_position)

    def count_visits(self):
        return len(self.track_tail_positions)

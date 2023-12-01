from common.FileReader import FileReader


class RopeBridge:
    def __init__(self, file_name="202209.txt", file_reader=FileReader()):
        self.file_reader = file_reader
        self.file_name = file_name
        self.data = self.file_reader.read_txt(self.file_name)

    def solve_part_one(self):
        moves = [RopeMove.parse(move) for move in self.data]
        print(moves)


class RopeMove:
    def __init__(self, direction, distance):
        self.direction = direction
        self.distance = distance

    @staticmethod
    def parse(move):
        direction = move[0]
        distance = int(move[1:])
        return RopeMove(direction, distance)

    def __repr__(self):
        return f"RopeMove({self.direction}, {self.distance})"


# H moves, then T moves (maybe)
# track the moves, and count the moves
class Board:
    def __init__(self):
        self.moves = []

    def add_move(self, move):
        self.moves.append(move)

    def count_visits(self):
        pass

    def next_move(self, move):
        pass

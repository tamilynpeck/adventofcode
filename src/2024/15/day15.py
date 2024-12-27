DIRECTIONS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


class Day15:
    def __init__(self, data):
        self.location = (0, 0)
        self.data = []
        self.moves = []
        moves = False
        for row in data:
            if row == "":
                moves = True
                continue
            if not moves:
                self.data.append(list(row))
            else:
                self.moves.extend(list(row))

        self.print_data()

    def print_data(self):
        for row in self.data:
            print("".join(row))

    def solve_part_one(self):
        for r, row in enumerate(self.data):
            for c, col in enumerate(row):
                if col == "@":
                    self.location = (r, c)

        for move in self.moves:
            self.handle_move(move)

        self.print_data()
        return self.count_box_scores()

    def handle_move(self, direction):

        move_to = (
            self.location[0] + DIRECTIONS[direction][0],
            self.location[1] + DIRECTIONS[direction][1],
        )

        if self.data[move_to[0]][move_to[1]] == "#":
            return

        # move box if able
        if self.data[move_to[0]][move_to[1]] == "O":
            self.move_box(move_to, direction)

        if self.data[move_to[0]][move_to[1]] == ".":
            self.data[self.location[0]][self.location[1]] = "."
            self.data[move_to[0]][move_to[1]] = "@"
            self.location = move_to
            return

    def move_box(self, from_loc, direction):
        move_to = (
            from_loc[0] + DIRECTIONS[direction][0],
            from_loc[1] + DIRECTIONS[direction][1],
        )

        if self.data[move_to[0]][move_to[1]] == "O":
            self.move_box(move_to, direction)

        if self.data[move_to[0]][move_to[1]] == ".":
            self.data[from_loc[0]][from_loc[1]] = "."
            self.data[move_to[0]][move_to[1]] = "O"

    def count_box_scores(self):
        scores = []
        for r, row in enumerate(self.data):
            for c, col in enumerate(row):
                if col == "O":
                    score = 100 * r + c
                    scores.append(score)

        return sum(scores)

    def solve_part_two(self):
        pass

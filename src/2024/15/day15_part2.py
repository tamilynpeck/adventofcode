DIRECTIONS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


class Day15Part2:
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
                temp_row = self.expand_row(row)
                self.data.append(list(temp_row))
            else:
                self.moves.extend(list(row))
        self.print_data()

    def print_data(self):
        for row in self.data:
            print("".join(row))
        print("-------------")

    def solve_part_two(self):
        # expand the grid
        for r, row in enumerate(self.data):
            for c, col in enumerate(row):
                if col == "@":
                    self.location = (r, c)

        for move in self.moves:
            self.handle_move(move)
        return self.count_box_scores()

    def handle_move(self, direction):
        move_to = (
            self.location[0] + DIRECTIONS[direction][0],
            self.location[1] + DIRECTIONS[direction][1],
        )

        if self.data[move_to[0]][move_to[1]] == "#":
            return

        # move box if able
        if self.data[move_to[0]][move_to[1]] in ["[", "]"]:
            self.move_box_pair(move_to, direction)

        if self.data[move_to[0]][move_to[1]] == ".":
            self.data[self.location[0]][self.location[1]] = "."
            self.data[move_to[0]][move_to[1]] = "@"
            self.location = move_to
            return

    def move_box_row(self, from_loc, direction):
        move_to = (
            from_loc[0] + DIRECTIONS[direction][0],
            from_loc[1] + DIRECTIONS[direction][1],
        )

        value = self.data[from_loc[0]][from_loc[1]]

        if value in ["[", "]"]:
            self.move_box_row(move_to, direction)

        if self.data[move_to[0]][move_to[1]] == ".":
            self.data[from_loc[0]][from_loc[1]] = "."
            self.data[move_to[0]][move_to[1]] = value

    def move_box_pair(self, from_loc, direction):
        print("move_box_pair", from_loc, direction)

        if direction in ["<", ">"]:
            self.move_box_row(from_loc, direction)
            return

        if not self.can_move_box_pair(from_loc, direction):
            return

        pair_loc = self.get_pair_loc(from_loc)
        move_to = (
            from_loc[0] + DIRECTIONS[direction][0],
            from_loc[1] + DIRECTIONS[direction][1],
        )
        move_pair_to = (
            pair_loc[0] + DIRECTIONS[direction][0],
            pair_loc[1] + DIRECTIONS[direction][1],
        )

        move_to_value = self.data[move_to[0]][move_to[1]]
        if move_to_value in ["[", "]"]:
            self.move_box_pair(move_to, direction)

        move_pair_to_value = self.data[move_pair_to[0]][move_pair_to[1]]
        if move_pair_to_value in ["[", "]"]:
            self.move_box_pair(move_pair_to, direction)

        move_to_value = self.data[move_to[0]][move_to[1]]
        move_pair_to_value = self.data[move_pair_to[0]][move_pair_to[1]]
        value = self.data[from_loc[0]][from_loc[1]]
        pair_value = self.data[pair_loc[0]][pair_loc[1]]
        if move_to_value == "." and move_pair_to_value == ".":
            self.data[from_loc[0]][from_loc[1]] = "."
            self.data[pair_loc[0]][pair_loc[1]] = "."
            self.data[move_to[0]][move_to[1]] = value
            self.data[move_pair_to[0]][move_pair_to[1]] = pair_value

    def can_move_box_pair(self, from_loc, direction):
        pair_loc = self.get_pair_loc(from_loc)
        move_to = (
            from_loc[0] + DIRECTIONS[direction][0],
            from_loc[1] + DIRECTIONS[direction][1],
        )
        move_pair_to = (
            pair_loc[0] + DIRECTIONS[direction][0],
            pair_loc[1] + DIRECTIONS[direction][1],
        )

        if self.data[move_to[0]][move_to[1]] == "#":
            return False
        if self.data[move_pair_to[0]][move_pair_to[1]] == "#":
            return False
        if self.data[move_to[0]][move_to[1]] in ["[", "]"]:
            if not self.can_move_box_pair(move_to, direction):
                return False
        if self.data[move_pair_to[0]][move_pair_to[1]] in ["[", "]"]:
            if not self.can_move_box_pair(move_pair_to, direction):
                return False
        return True

    def get_pair_loc(self, from_loc):
        if self.data[from_loc[0]][from_loc[1]] == "[":
            return (from_loc[0], from_loc[1] + 1)
        return (from_loc[0], from_loc[1] - 1)

    def count_box_scores(self):
        scores = []
        for r, row in enumerate(self.data):
            for c, col in enumerate(row):
                if col == "[":
                    score = 100 * r + c
                    scores.append(score)

        return sum(scores)

    def expand_row(self, row):
        row = row.replace("#", "##")
        row = row.replace("O", "[]")
        row = row.replace(".", "..")
        row = row.replace("@", "@.")
        return row

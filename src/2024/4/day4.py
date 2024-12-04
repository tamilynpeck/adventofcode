class Day4:
    def __init__(self, data):
        self.data = data
        for row in self.data:
            print(row)

    def solve_part_one(self):
        xmas_count = 0
        for r, row in enumerate(self.data):
            for c, char in enumerate(row):
                if char == "X":
                    result = self.search_for_xmas(r, c)
                    if result > 0:
                        print("found xmas", r, c)
                        xmas_count += result
        return xmas_count

    def solve_part_two(self):
        xmas_count = 0
        for r, row in enumerate(self.data):
            for c, char in enumerate(row):
                if char == "A":
                    if self.search_for_x_of_mas(r, c):
                        print("found x-mas", r, c)
                        xmas_count += 1
        return xmas_count

    def search_for_xmas(self, r, c):
        locations = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
            [1, 1],
            [1, -1],
            [-1, 1],
            [-1, -1],
        ]

        xmas_found = 0
        for x, y in locations:
            new_x, new_y = r + x, c + y
            # if found, keep doing in that direction...
            if self.search_for_char(new_x, new_y, "M"):
                if self.search_for_char(new_x + x, new_y + y, "A"):
                    if self.search_for_char(new_x + (x * 2), new_y + (y * 2), "S"):
                        xmas_found += 1

        return xmas_found

    def search_for_x_of_mas(self, r, c):
        # search both diagonals, for MAS
        # [1, 1], [-1, -1],
        result = self.get_char(r + 1, c + 1), self.get_char(r - 1, c - 1)
        if not result == ("M", "S") and not result == ("S", "M"):
            return False
        # [1, -1], [-1, 1],
        result = self.get_char(r + 1, c - 1), self.get_char(r - 1, c + 1)
        if not result == ("M", "S") and not result == ("S", "M"):
            return False
        return True

    def search_for_char(self, x, y, char):
        if x < 0 or y < 0:
            return False
        try:
            if self.data[x][y] == char:
                return True
        except IndexError:
            return False

        return False

    def get_char(self, x, y):
        if x < 0 or y < 0:
            return None
        try:
            return self.data[x][y]
        except IndexError:
            return None

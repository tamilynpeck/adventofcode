class Day12:
    def __init__(self, data):
        self.data = data

    def solve_part_one(self):
        data = self.data[0]
        grid = {
            i + j * 1j: c
            for i, r in enumerate(self.data)
            for j, c in enumerate(r.strip())
        }
        print(grid)

        sets = {p: {p} for p in grid}

        for p in grid:
            for n in p + 1, p - 1, p + 1j, p - 1j:
                if n in grid and grid[p] == grid[n]:
                    sets[p] |= sets[n]
                    for x in sets[p]:
                        sets[x] = sets[p]

        sets = {tuple(s) for s in sets.values()}

        print(sets)

    def solve_part_two(self):
        pass

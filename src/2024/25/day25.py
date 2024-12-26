class Day25:
    def __init__(self, data):
        self.data = data
        print(self.data)
        self.locks = []
        self.keys = []

        for i, row in enumerate(self.data):
            if row == "#####" and (i == 0 or self.data[i - 1] == ""):
                print("lock")
                counts = [0, 0, 0, 0, 0]
                values = [x for x in self.data[i + 1 : i + 6]]
                for value in values:
                    for j, char in enumerate(value):
                        if char == "#":
                            counts[j] += 1
                print(counts)
                self.locks.append(counts)
            elif row == "....." and (i == 0 or self.data[i - 1] == ""):
                print("key")
                counts = [0, 0, 0, 0, 0]
                values = [x for x in self.data[i + 1 : i + 6]]
                for value in values:
                    for j, char in enumerate(value):
                        if char == "#":
                            counts[j] += 1
                print(counts)
                self.keys.append(counts)
            else:
                continue

    def solve_part_one(self):
        matches = 0
        for key in self.keys:
            for lock in self.locks:
                if self.key_matches_lock(key, lock):
                    matches += 1

        return matches

    def solve_part_two(self):
        pass

    def key_matches_lock(self, key, lock):
        for i, key_value in enumerate(key):
            if key_value + lock[i] > 5:
                return False
        return True

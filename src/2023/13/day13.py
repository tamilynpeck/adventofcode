from collections import Counter


class Day13:
    def __init__(self, data):
        self.data = data
        self.patterns = []

    def solve_part_one(self):
        self.parse_data()
        print(self.patterns)
        scores = 0

        for _, pattern in enumerate(self.patterns):
            vertical_match = self.score_vertical_pattern(pattern)
            if vertical_match:
                print("vertical_match", vertical_match)
                scores += vertical_match
            horizontal_match = self.score_horizontal_pattern(pattern)
            if horizontal_match:
                print("horizontal_match", horizontal_match)
                scores += horizontal_match * 100

        return scores

    def solve_part_two(self):
        pass

    def score_vertical_pattern(self, pattern):
        transposed = ["".join(r) for r in zip(*pattern)]

        return self.score_horizontal_pattern(transposed)

    def score_horizontal_pattern(self, pattern):
        # compare 0 and 1, = i - 0 and i + 1, continue
        # compare 1 and 2, 0 and 3 = i - 0 and i + 1, i - 1 and i + 2
        # compare 2 and 3, 1 and 4, 0 and 5 = i - 0 and i + 1, i - 1 and i + 2, i - 2 and i + 3
        # compare 3 and 4, 2 and 5, 0 and 6, 0 and 7 = i - 0 and i + 1, i - 1 and i + 2, i - 2 and i + 3, i - 3 and i + 4

        for i, _ in enumerate(pattern):
            remaining = len(pattern) - i
            match = False
            for j in range(remaining):
                index1, index2 = i - j, i + j + 1
                if index1 < 0:
                    break
                # print(i, j, ":", index1, index2)
                if index1 > len(pattern) - 1 or index2 > len(pattern) - 1:
                    continue
                if pattern[index1] == pattern[index2]:
                    match = True
                    # print("match", index1, index2, pattern[index1])
                else:
                    match = False
                    break

            if match:
                # print("match", i, pattern[i])
                return i + 1

        return None

    def parse_data(self):
        pattern = []
        for line in self.data:
            if line:
                pattern.append(line)
            else:
                self.patterns.append(pattern)
                pattern = []
        self.patterns.append(pattern)

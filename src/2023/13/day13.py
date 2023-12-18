from collections import Counter


class Day13:
    def __init__(self, data):
        self.data = data
        # print(data)
        self.patterns = []

    def solve_part_one(self):
        self.parse_data()
        print(self.patterns)
        odd_scores = 0
        even_scores = 0

        for i, pattern in enumerate(self.patterns):
            if i % 2 == 0:
                print("score_even_pattern")
                even_scores += self.score_even_pattern(pattern)
            else:
                print("score_odd_pattern")
                # odd_scores += self.score_odd_pattern(pattern)

    def solve_part_two(self):
        pass

    def score_even_pattern(self, pattern):
        # find vertical reflection
        matches = []
        for c, line in enumerate(pattern):
            row = [l for l in line]
            print(c, row)
            for i in range(len(row)):
                test_column = row[:i]
                test_mirror_column = row[i:]
                min_len = min(len(test_column), len(test_mirror_column))
                print(i, min_len, test_column[:min_len], test_mirror_column[:min_len])

                if (
                    test_column
                    and test_column[:min_len] == test_mirror_column[:min_len]
                ):
                    print("match", c, i)
                    matches.append(i)

        if matches:
            # get match where value equals len(pattern)
            get_matches = Counter(matches).most_common(1)
            print("matches", Counter(matches))
            print("get_matches", get_matches)
            # most common + 1

        return 0

    def score_odd_pattern(self, pattern):
        # find horizontal reflection
        row_len = len(pattern[0])
        matches = []
        for c in range(row_len):
            column = [line[c] for line in pattern]
            print(c, column)
            for i in range(len(column)):
                test_column = column[:i]
                test_mirror_column = column[i:]
                min_len = min(len(test_column), len(test_mirror_column))
                print(test_column[:min_len], test_mirror_column[:min_len])
                # min_len = min(len(test_column), len(test_reversed_column))
                if (
                    test_column
                    and test_column[:min_len] == test_mirror_column[:min_len]
                ):
                    print("match", c, i)
                    matches.append(i)

        if matches:
            # get match where value equals len(pattern[0])
            get_matches = Counter(matches).most_common(1)
            print("matches", Counter(matches))
            print("get_matches", get_matches)
            # most common + 1
        return 0

    def parse_data(self):
        pattern = []
        for line in self.data:
            if line:
                pattern.append(line)
            else:
                self.patterns.append(pattern)
                pattern = []
        self.patterns.append(pattern)

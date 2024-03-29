class Pattern:
    length = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    legnth_in = {5: [2, 3, 5], 6: [0, 6, 9]}
    contained = {
        2: [8],
        3: [8],
        5: [6, 8],
        0: [8],
        6: [8],
        9: [8],
    }
    contains = {
        2: [],
        3: [1, 7],
        5: [],
        0: [1, 7],
        6: [],
        9: [1, 4, 7],
    }

    def __init__(self, codes):
        self.codes = codes
        self.key = {}
        self.functions = {
            1: lambda x: self.matching_length(2),  # fix magic numbers...
            4: lambda x: self.matching_length(4),
            7: lambda x: self.matching_length(3),
            8: lambda x: self.matching_length(7),
            2: lambda x: self.matching_two_and_six(2),
            6: lambda x: self.matching_two_and_six(6),
            # 6,
        }
        for key, function in self.functions.items():
            code = function(key)
            self.key[key] = code
            print(self.key)
        self.key = {value: key for key, value in self.key.items()}
        print(self.key)

    def matching_length(self, legnth: int):
        return [code for code in self.codes if len(code) == legnth][0]

    def matching_two_and_six(self, number):
        expected_length = Pattern.length[number]
        remaining = [code for code in self.codes if len(code) == expected_length]
        # options = Pattern.legnth_in[Pattern.length[number]]
        for code in remaining:
            print("for code", code)
            contains_pattern = [
                k for k, v in self.key.items() if Pattern.contains_values(code, v)
            ]
            for value in Pattern.legnth_in[expected_length]:
                if contains_pattern == Pattern.contains[value]:
                    return code
            print(contains_pattern)

        return None

    def contains_values(value1, value2):
        print(value1, value2)
        if len(value1) < len(value2):
            return False
        for letter in value2:
            if letter not in [l for l in value1]:
                return False
        return True

    def contained_in(value1, value2):
        print(value1, value2)
        if len(value1) > len(value2):
            return False
        for letter in value2:
            if letter not in [l for l in value1]:
                return False
        return True


class SevenSegmentSearch:
    def __init__(self, input):
        self.input = input
        self.unique_length = {2: 1, 3: 7, 4: 4, 7: 8}
        self.unique_lengths = [2, 4, 3, 7]

    @staticmethod
    def parse_input(file):
        with open(file) as input_file:
            numbers = [line.strip() for line in input_file.readlines()]
            input = [n.split(" | ") for n in numbers]
        return {x: y.split(" ") for x, y in input}

    def count_unique_output_values(self):
        counts = 0
        for key, value in self.input.items():
            code = key.split(" ")
            uniques = [n for n in value if len(n) in self.unique_lengths]
            counts += len(uniques)
        return counts

    def decode_pattern(self, code):
        codes = code.split(" ")
        print(codes)
        pattern = {}
        for code in codes:
            if len(code) in self.unique_lengths:
                pattern[code] = self.unique_length[len(code)]
        codes = [code for code in codes if len(code) not in self.unique_lengths]
        print(codes)
        for code in codes:
            options = Pattern.legnth_in[len(code)]
            for option in options:
                checks = Pattern.contained[option]
                match = True
                for check in checks:
                    for letter in code:
                        if letter in codes[check]:
                            pass

        print(pattern)

        return pattern

class Day3:
    def __init__(self, data):
        self.data = data

    def solve_part_one(self):
        joltages = []

        for line in self.data:
            joltages.append(self.find_maximum_joltage(line))

        return sum(joltages)

    def solve_part_two(self):
        pass

    def find_maximum_joltage(self, line):
        digits = [int(d) for d in line]
        jolt = ""

        # max digit except last
        max_index = digits.index(max(digits[: len(digits) - 1]))
        max_digit = digits[max_index]
        jolt += str(max_digit)

        remaining = digits[max_index + 1 :]
        next_max = max(remaining)
        jolt += str(next_max)

        return int(jolt)

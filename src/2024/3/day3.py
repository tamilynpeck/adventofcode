import re


class Day3:
    def __init__(self, data):
        self.data = "".join(data)

    def solve_part_one(self):
        regex = r"mul\((\d+),(\d+)\)"
        matches = re.findall(regex, self.data)
        result = [int(match[0]) * int(match[1]) for match in matches]
        return sum(result)

    def solve_part_two(self):
        regex = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
        matches = re.findall(regex, self.data)
        result = 0
        enabled = True
        for match in matches:
            if match == "do()" :
                enabled = True
            elif match == "don't()":
                enabled = False
            elif enabled:
                match = re.findall(r"\d+", match)
                result += int(match[0]) * int(match[1])

        return result

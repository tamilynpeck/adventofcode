from functools import cache


class Day19:
    def __init__(self, data):
        self.data = data
        self.available = data[0].split(", ")
        self.designs = data[2:]
        self.patterns = self.available

    def solve_part_one(self):
        possible_designs = 0
        for i, design in enumerate(self.designs):
            self.patterns = self.available
            print(f"Checking design {i + 1} - {design}")
            if self.is_possible(design):
                possible_designs += 1

        return possible_designs

    def solve_part_two(self):
        possible_designs = 0
        for i, design in enumerate(self.designs):
            self.patterns = self.available
            print(f"Checking design {i + 1} - {design}")
            possible_designs += self.how_many_possible(design)

        return possible_designs

    @cache
    def is_possible(self, design):
        self.patterns = [a for a in self.patterns if a in design]

        if len(design) == 0:
            return True
        for a in self.patterns:
            if len(a) <= len(design) and a == design[: len(a)]:
                # print(f"{design} Found " + a, "Starting with " + design[len(a) :])
                if self.is_possible(design.removeprefix(a)):
                    return True

        return False

    @cache
    def how_many_possible(self, design):
        self.patterns = [a for a in self.patterns if a in design]

        if len(design) == 0:
            return 1
        possible_designs = 0
        for a in self.patterns:
            if len(a) <= len(design) and a == design[: len(a)]:
                # print(f"{design} Found " + a, "Starting with " + design[len(a) :])
                possible_designs += self.is_possible(design.removeprefix(a))

        return possible_designs

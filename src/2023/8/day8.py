from math import lcm


class Day8:
    def __init__(self, data):
        self.data = data
        self.directions = data[0]
        self.instructions = data[2:]
        self.map = parse_instructions(self.instructions)

    def solve_part_one(self):
        start_location = "AAA"
        steps = self.get_steps_to_dest(start_location, dest=lambda x: x == "ZZZ")
        return steps

    def solve_part_two(self):
        start_locations = [l for l in self.map.keys() if l.endswith("A")]
        steps_to_dests = []

        for location in start_locations:
            steps = self.get_steps_to_dest(location, dest=lambda x: x.endswith("Z"))
            steps_to_dests.append(steps)

        return lcm(*steps_to_dests)

    def get_steps_to_dest(self, start_location, dest):
        location = start_location
        steps = 0
        looking = True
        while looking:
            for direction in self.directions:
                location = self.map[location][direction]
                steps += 1
                if dest(location):
                    looking = False
                    break

        return steps


def parse_instructions(instructions):
    map = {}
    for instruction in instructions:
        key, dirs = instruction.split("=")
        key = key.strip()
        dirs = dirs.strip().replace("(", "").replace(")", "").split(",")
        dirs = [dir.strip() for dir in dirs]
        dirs = {"L": dirs[0], "R": dirs[1]}
        map[key] = dirs

    return map

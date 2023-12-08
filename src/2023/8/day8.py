class Day8:
    def __init__(self, data):
        self.data = data
        self.directions = data[0]
        self.instructions = data[2:]
        self.map = parse_instructions(self.instructions)
        self.location = "AAA"
        self.steps = 0

    def solve_part_one(self):
        looking = True
        while looking:
            for direction in self.directions:
                # print(self.location, direction)
                if direction == "R":
                    self.location = self.map[self.location][1]
                elif direction == "L":
                    self.location = self.map[self.location][0]

                self.steps += 1
                if self.location == "ZZZ":
                    looking = False

        return self.steps

    def solve_part_two(self):
        self.locations = [
            location for location in self.map.keys() if location.endswith("A")
        ]
        print(self.locations)

        looking = True
        # i = 0
        while looking:
            for direction in self.directions:
                if direction == "R":
                    self.locations = [
                        self.map[location][1] for location in self.locations
                    ]
                elif direction == "L":
                    self.locations = [
                        self.map[location][0] for location in self.locations
                    ]

                self.steps += 1
                if all([location.endswith("Z") for location in self.locations]):
                    looking = False
            # i += 1
            # if i > 100:
            #     break

        return self.steps


def parse_instructions(instructions):
    map = {}
    for instruction in instructions:
        key, dirs = instruction.split("=")
        key = key.strip()
        dirs = dirs.strip().replace("(", "").replace(")", "").split(",")
        dirs = [dir.strip() for dir in dirs]
        map[key] = dirs

    return map

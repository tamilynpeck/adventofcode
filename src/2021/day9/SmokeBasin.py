class SmokeBasin:
    def __init__(self, input):
        pass

    @staticmethod
    def parse_input(file):
        with open(file) as input_file:
            numbers = [line.strip() for line in input_file.readlines()]
            input = [n.split(" | ") for n in numbers]
        return input

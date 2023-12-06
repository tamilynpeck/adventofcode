class TuningTrouble:
    def __init__(self, data):
        self.data = data[0]

    def solve_part_one(self):
        return TuningTrouble.solve(self.data, packet_size=4)

    def solve_part_two(self):
        return TuningTrouble.solve(self.data, packet_size=14)

    @staticmethod
    def solve(data, packet_size):
        length = len(data)
        for i in range(packet_size, length):
            test_marker = data[i - packet_size : i]
            if len(set(char for char in test_marker)) == packet_size:
                return i

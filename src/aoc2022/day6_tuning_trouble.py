from common.FileReader import FileReader


class TuningTrouble:
    def __init__(self, file_name="202206.txt", file_reader=FileReader()):
        self.file_name = file_name
        self.file_reader = file_reader
        self.data_stream = self.file_reader.read_txt(self.file_name)[0]

    def solve_part_one(self):
        return TuningTrouble.solve(self.data_stream, packet_size=4)

    def solve_part_two(self):
        return TuningTrouble.solve(self.data_stream, packet_size=14)

    @staticmethod
    def solve(data_stream, packet_size):
        length = len(data_stream)
        for i in range(packet_size, length):
            test_marker = data_stream[i - packet_size : i]
            if len(set(char for char in test_marker)) == packet_size:
                return i

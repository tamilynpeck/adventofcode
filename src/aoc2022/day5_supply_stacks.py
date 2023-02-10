from common.FileReader import FileReader


class SupplyStacks:
    def __init__(self, file_name="202205.txt", file_reader=FileReader()):
        data = file_reader.read_txt(file_name)
        self.crates, self.moves = SupplyStacks.parse_data(data)

    def part_one(self):
        print(self.stacks)
        print(self.moves)

    def sort_crates(self):
        pass

    @staticmethod
    def parse_data(data):
        crates = [row for row in data if row and not row.startswith("move")]
        moves = [row for row in data if row.startswith("move")]

        return crates, moves

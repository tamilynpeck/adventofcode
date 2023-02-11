from common.FileReader import FileReader


# class CrateNode:
#     def __init__(self, row):
#         self.row = row

test_data = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3"""


class Stacks:
    def __init__(self, crate_data):
        self.crate_data = crate_data

    @staticmethod
    def create_stacks(stacks):
        # labels = stacks.pop()
        # print(labels)
        column_char_width = 3
        labels = [int(char) for char in stacks.pop() if char.isdigit()]
        crate_data = {key: None for key in stacks}
        print(labels)
        print(stacks)
        # 0 - 3
        # 5-8
        # 1*3 + 1*1

        # 2*3 + 2*1
        for label, i in enumerate(labels):
            crate_data[label] = stacks[i : i + column_char_width].strip("[").strip("]")

        return Stacks(crate_data)

    def organize_creates(self, moves):
        pass


class SupplyStacks:
    def __init__(self, file_name="202205.txt", file_reader=FileReader()):
        data = file_reader.read_txt(file_name)
        self.stacks, self.moves = SupplyStacks.parse_data(data)

    def part_one(self):
        print(self.stacks)
        print(self.moves)

        stacks = Stacks.create_stacks(self.stacks)
        stacks.organize_creates(self.moves)

    def sort_crates(self):
        pass

    @staticmethod
    def parse_data(data):
        stacks = [row for row in data if row and not row.startswith("move")]
        moves = [row for row in data if row.startswith("move")]

        return stacks, moves

from common.FileReader import FileReader


# class CrateNode:
#     def __init__(self, row):
#         self.row = row


class Stacks:
    def __init__(self, crate_data):
        self.crate_data = crate_data

    @staticmethod
    def create_stacks(stacks):
        column_char_width = 3
        column_space_width = 1
        labels = [int(char) for char in stacks.pop() if char.isdigit()]
        max_len = max([len(row) for row in stacks])
        stacks = [row.ljust(max_len, " ") for row in stacks]
        crate_data = {key: [] for key in labels}
        # print(labels)
        # print(stacks)

        for i, label in enumerate(labels):
            index = i * column_char_width + i * column_space_width
            # print(index)
            for stack in stacks:
                # print(len(stack), stack)
                crate = stack[index + 1].strip()
                if crate:
                    crate_data[label].insert(0, crate)

        print(crate_data)
        return Stacks(crate_data)

    def organize_crates(self, moves):
        # move 1 from 2 to 1
        # m[0] count, m[1] from #, m[2] to #
        for move in moves:
            print(move)
            m = [int(char) for char in move if char.isdigit()]
            for i in range(0, m[0]):
                crate = self.crate_data[m[1]].pop()
                self.crate_data[m[2]].append(crate)


class SupplyStacks:
    def __init__(self, file_name="202205.txt", file_reader=FileReader()):
        data = file_reader.read_txt(file_name)
        self.stacks, self.moves = SupplyStacks.parse_data(data)

    def part_one(self):
        print(self.stacks)
        print(self.moves)

        stacks = Stacks.create_stacks(self.stacks)
        stacks.organize_crates(self.moves)

    def sort_crates(self):
        pass

    @staticmethod
    def parse_data(data):
        stacks = [row for row in data if row and not row.startswith("move")]
        moves = [row for row in data if row.startswith("move")]

        return stacks, moves
